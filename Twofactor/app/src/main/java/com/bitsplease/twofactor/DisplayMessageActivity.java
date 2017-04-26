package com.bitsplease.twofactor;

import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.TextView;

import java.io.UnsupportedEncodingException;
import java.nio.ByteBuffer;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.Arrays;
import java.util.Date;

public class DisplayMessageActivity extends AppCompatActivity {

    private final static char[] hexArray = "0123456789abcdef".toCharArray();
    public String bytesToHex(byte[] bytes) {
        char[] hexChars = new char[bytes.length * 2];
        for ( int j = 0; j < bytes.length; j++ ) {
            int v = bytes[j] & 0xFF;
            hexChars[j * 2] = hexArray[v >>> 4];
            hexChars[j * 2 + 1] = hexArray[v & 0x0F];
        }
        return new String(hexChars);
    }

    public int TOTP(String secret) {
        MessageDigest digest = null;
        Date date = new Date();
        long time = date.getTime() / 1000;
        time = time / 30;
        try {
            digest = MessageDigest.getInstance("SHA-1");
        } catch (NoSuchAlgorithmException e) {
            e.printStackTrace();
        }
        digest.reset();
        try {
            digest.update((secret + time).getBytes("utf8"));
        } catch (UnsupportedEncodingException e) {
            e.printStackTrace();
        }

        secret = secret + bytesToHex(digest.digest());

        try {
            digest = MessageDigest.getInstance("SHA-1");
        } catch (NoSuchAlgorithmException e) {
            e.printStackTrace();
        }
        digest.reset();
        try {
            digest.update(secret.getBytes("utf8"));
        } catch (UnsupportedEncodingException e) {
            e.printStackTrace();
        }

        byte[] small = Arrays.copyOfRange(digest.digest(), 15, 19);
        ByteBuffer wrapped = ByteBuffer.wrap(small);
        int num = wrapped.getInt();

        if (num < 0)
            num = -num;
        num = num % 1000000;
        int len = String.valueOf(num).length();
        if (len < 6) {
            num = num * (int) Math.pow(10, (6 - len));
        }

        return num;
    }
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        String secret = null;

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_display_message);

        SharedPreferences prefs = this.getSharedPreferences(
                "com.bitsplease.twofactor", Context.MODE_PRIVATE);
        secret = prefs.getString("secret", secret);

        if (secret == null) {
            // Get the Intent that started this activity and extract the string
            Intent intent = getIntent();
            prefs.edit().putString("secret", intent.getStringExtra(MainActivity.EXTRA_MESSAGE)).apply();
            secret = prefs.getString("secret", secret);
        }

        String message = Integer.toString(TOTP(secret));
        // Capture the layout's TextView and set the string as its text
        TextView textView = (TextView) findViewById(R.id.textViewC);
        textView.setText(message);
    }
}

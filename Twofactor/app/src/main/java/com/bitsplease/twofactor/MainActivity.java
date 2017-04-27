package com.bitsplease.twofactor;

import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {
    public static final String EXTRA_MESSAGE = "com.bitsplease.twofactor.MESSAGE";
    public String secret;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        SharedPreferences prefs = this.getSharedPreferences(
                "com.bitsplease.twofactor", Context.MODE_PRIVATE);
        secret = prefs.getString("secret", secret);
        if (secret == null)
            setContentView(R.layout.activity_not_set);
        else
            setContentView(R.layout.activity_set);
    }

    /** Called when the user taps the Send button */
    public void sendMessage(View view) {
        Intent intent = new Intent(this, DisplayMessageActivity.class);
        EditText editText = (EditText) findViewById(R.id.editText);
        String message = editText.getText().toString();
        intent.putExtra(EXTRA_MESSAGE, message);
        startActivity(intent);
    }

    public void sendEmptyMessage(View view) {
        Intent intent = new Intent(this, DisplayMessageActivity.class);
        startActivity(intent);
    }

    public void reset(View view) {
        Intent intent = new Intent(this, ResetActivity.class);
        startActivity(intent);
    }
}

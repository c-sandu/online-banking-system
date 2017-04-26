package com.bitsplease.twofactor;

import android.content.Context;
import android.content.SharedPreferences;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;

public class ResetActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_reset);

        SharedPreferences prefs = this.getSharedPreferences(
                "com.bitsplease.twofactor", Context.MODE_PRIVATE);
        prefs.edit().putString("secret", null).apply();
    }
}

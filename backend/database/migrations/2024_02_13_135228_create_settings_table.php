<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;
use \App\Models\Setting;

return new class extends Migration
{
    /**
     * Run the migrations.
     */
    public function up(): void
    {
        Schema::create('settings', function (Blueprint $table) {
            $table->id();
            $table->enum('humanation_status', Setting::HUMANATION_STATUS)->default('stopped');
            $table->enum('account_creator_status', Setting::ACCOUNT_CREATOR_STATUS)->default('stopped');
            $table->enum('humanation_flow_status', Setting::HUMANATION_FLOW_STATUS)->default('idle');
            $table->enum('account_creator_flow_status', Setting::ACCOUNT_CREATOR_FLOW_STATUS)->default('idle');

            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('settings');
    }
};

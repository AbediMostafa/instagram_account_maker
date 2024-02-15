<?php

namespace Database\Factories;

use App\Models\Account;
use Illuminate\Database\Eloquent\Factories\Factory;

/**
 * @extends \Illuminate\Database\Eloquent\Factories\Factory<\App\Models\Account>
 */
class AccountFactory extends Factory
{
    /**
     * Define the model's default state.
     *
     * @return array<string, mixed>
     */
    public function definition(): array
    {
        return [
            'username'=>fake()->userName,
            'password'=>fake()->password,
            'phone'=>fake()->phoneNumber,
            'session'=>fake()->uuid,
            'instagram_status'=>fake()->randomElement(Account::INSTAGRAM_STATUS),
            'usage_status'=>fake()->randomElement(Account::USAGE_STATUS),
            'log'=>fake()->text
        ];
    }
}

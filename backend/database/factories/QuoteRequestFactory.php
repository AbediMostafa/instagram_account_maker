<?php

namespace Database\Factories;

use App\Models\QuoteRequest;
use Illuminate\Database\Eloquent\Factories\Factory;

/**
 * @extends \Illuminate\Database\Eloquent\Factories\Factory<\App\Models\QuoteRequest>
 */
class QuoteRequestFactory extends Factory
{
    /**
     * Define the model's default state.
     *
     * @return array<string, mixed>
     */
    public function definition(): array
    {
        return [
            'address'=>fake()->address,
            'number_of_stumps'=>fake()->randomElement(QuoteRequest::NUMBER_OF_STUMPS),
            'diameter_of_largest_tree'=>fake()->randomElement(QuoteRequest::DIAMETER_OF_LARGEST_TREE),
            'area'=>fake()->randomElement(QuoteRequest::AREA),
            'stump_position'=>fake()->randomElement(QuoteRequest::STUMP_POSITION),
            'current_stump_high_is_less_than_12'=>fake()->boolean(),
        ];
    }
}

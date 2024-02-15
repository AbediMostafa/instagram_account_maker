<?php

namespace Database\Seeders;

use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;
use Illuminate\Support\Facades\DB;

class AccountSeeder extends Seeder
{
    /**
     * Run the database seeds.
     */
    public function run(): void
    {
        DB::table('accounts')->insert([
            ['username'=>'sam238629', 'password'=>'far895tile620'],
            ['username'=>'surbonboysd11', 'password'=>'far895tile620'],
            ['username'=>'samanehghorunian', 'password'=>'far895tile620'],
            ['username'=>'saram_ough', 'password'=>'far895tile620'],
            ['username'=>'forugh361', 'password'=>'far895tile620'],
            ['username'=>'samo.ire', 'password'=>'far895tile620'],
            ['username'=>'fara.bi91', 'password'=>'far895tile620'],
            ['username'=>'douze232', 'password'=>'mosthegreate'],
            ['username'=>'zamari197', 'password'=>'far895tile620'],
            ['username'=>'sorou662', 'password'=>'far895tile620'],
            ['username'=>'goodi3386', 'password'=>'far895tile620'],
        ]);
    }
}

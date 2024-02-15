<?php

namespace App\Console\Commands;

use Illuminate\Console\Command;

class cc extends Command
{
    /**
     * The name and signature of the console command.
     *
     * @var string
     */
    protected $signature = 'cc';

    /**
     * The console command description.
     *
     * @var string
     */
    protected $description = 'Command description';

    /**
     * Execute the console command.
     */
    public function handle()
    {
        $this->call('cache:clear');
        $this->call('view:clear');
        $this->call('route:clear');
        $this->call('clear-compiled');
        $this->call('config:cache');
    }
}

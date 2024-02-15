<?php

use Illuminate\Support\Facades\Auth;
use Illuminate\Support\Facades\Route;
use \App\Http\Controllers\AuthController;
use \App\Http\Controllers\UserController;
use \App\Http\Controllers\RoleController;
use \App\Http\Controllers\QuoteRequestController;

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider and all of them will
| be assigned to the "web" middleware group. Make something great!
|
*/

Route::get('/', function () {
    dd(\App\Models\User::get()[3]);
});

Route::post('login', [AuthController::class, 'login']);
Route::post('signup', [AuthController::class, 'signup']);
Route::post('logout', [AuthController::class, 'logout']);
Route::post('users', [UserController::class, 'index']);
Route::post('user/edit', [UserController::class, 'edit']);
Route::post('user/update', [UserController::class, 'update']);
Route::post('user/create', [UserController::class, 'create']);
Route::post('user/delete', [UserController::class, 'delete']);
Route::post('user/reset-password', [UserController::class, 'resetPassword']);
Route::post('roles', [RoleController::class, 'index']);
Route::post('quotes', [QuoteRequestController::class, 'index']);
Route::post('quote/apis', [QuoteRequestController::class, 'apis']);
Route::post('quote/create', [QuoteRequestController::class, 'create']);
Route::post('quote/show', [QuoteRequestController::class, 'show']);
Route::post('quote/delete', [QuoteRequestController::class, 'delete']);

Route::middleware('auth:sanctum')->group(function () {



});


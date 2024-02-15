<?php

namespace App\Http\Controllers;

use App\Models\User;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;
use Illuminate\Support\Facades\Hash;

class UserController extends Controller
{

    public function index()
    {

        return User::select(
            'id',
            'name',
            'email'
        )
            ->withCount('quoteRequests')
            ->with('roles:id,name')
            ->paginate(10);
    }

    public function create()
    {
        \request()->validate([
            'name' => 'required',
            'email' => 'required|unique:users,email',
        ]);

        return tryCatch(
            function () {
                $user = User::create([
                    'name' => r('name'),
                    'email' => r('email'),
                    'password' => Hash::make(r('password')),
                ]);

                $user && $user->roles()->attach(r('role'));
            },
            'User created successfully',
            'Problem creating user',
        );
    }

    public function delete()
    {

        return tryCatch(
            fn() => User::whereId(r('userId'))->delete()
            ,
            'User deleted successfully',
            'Problem deleting user',
        );
    }

    public function edit()
    {
        return User::select(
            'id',
            'name',
            'email'
        )
            ->with('roles:id,name')
            ->findOrFail(r('userId'));
    }

    public function update()
    {
        \request()->validate([
            'name' => 'required',
            'email' => 'required|unique:users,email,' . r('id'),
        ]);

        return tryCatch(
            fn() => User::whereId(r('id'))->update(r()->except(['id', 'role']))
            , 'User updated successfully'
            , 'Problem updating user'
        );
    }

    public function resetPassword()
    {
        return tryCatch(
            fn() => User::whereId(r('userId'))
                ->update(['password' => Hash::make(r('password'))]),
            'Password updated successfully',
            'Problem updating password',
        );
    }
}

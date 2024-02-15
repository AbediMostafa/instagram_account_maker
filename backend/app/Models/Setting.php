<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Setting extends Model
{
    use HasFactory;

    const HUMANATION_STATUS=['started', 'stopped'];
    const ACCOUNT_CREATOR_STATUS=['started', 'stopped'];
    const HUMANATION_FLOW_STATUS=['idle','pick account', 'see timeline', 'follow', 'see explore', ];
    const ACCOUNT_CREATOR_FLOW_STATUS=['idle'];
}

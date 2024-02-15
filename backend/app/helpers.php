<?php

/**
 * Return error status and message to the front
 *
 * @param $msg
 * @param bool|array $additional
 * @return array
 */
function jsonError($msg, bool|array $additional = []): array
{
    return $additional ?
        [
            'withResponse' => true,
            'status' => 0,
            'msg' => $msg,
            ...$additional
        ] :
        [
            'withResponse' => true,
            'status' => 0,
            'msg' => $msg
        ];
}

/**
 * Return success status and message to the front
 *
 * @param $msg
 * @param bool|array $additional
 * @return array
 */
function jsonSuccess($msg, bool|array $additional = []): array
{
    return $additional ?
        [
            'withResponse' => true,
            'status' => 1,
            'msg' => $msg,
            ...$additional
        ] :
        [
            'withResponse' => true,
            'status' => 1,
            'msg' => $msg,
        ];
}

/**
 * A shorthand of request method
 *
 * @return array|\Illuminate\Contracts\Foundation\Application|\Illuminate\Http\Request|mixed|string|null
 */
function r($value = ''): mixed
{
    return $value ? request($value) : request();
}

/**
 * Simplifies try catch block
 *
 * @param $callB
 * @param $successMsg
 * @param $errorMsg
 * @return array
 */
function tryCatch($callB, $successMsg, $errorMsg)
{
    try {
        $callB();

        return jsonSuccess($successMsg);

    } catch (Exception $e) {

        if (get_class($e) === 'Symfony\Component\HttpKernel\Exception\HttpException') {
            throw new HttpException(422, $e->getMessage());
        }

        /**
         * TODO : in production mode replace with $errorMsg
         */
        return jsonError($e->getMessage());
    }
}

function abortIf($condition): void
{
    abort_if($condition, 403, 'You dont have permission to see this page');
}

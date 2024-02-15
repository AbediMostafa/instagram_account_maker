import {defineStore} from "pinia";
import router from "@/router";
import ApiService from "@/core/services/ApiService";

export const useAuthStore = defineStore("auth", {

    state() {
        return {
            user: null,
        }
    },

    actions: {

        setUser(authUser: any) {
            if (typeof authUser === 'object') {
                this.user = authUser
                const user = JSON.stringify(authUser)
                return localStorage.setItem('user', user)
            }

            throw new Error(`Cannot set user because ${authUser} is not object`)
        },

        getUser() {
            return this.user;
        },

        purgeUser() {
            localStorage.removeItem('user');
            this.user = null
        },
        reAssignUser() {
            const user = localStorage.getItem('user');

            if (user) {
                return this.user = JSON.parse(user)
            }

            this.purgeUser();
        },

        logout() {
            ApiService.post('logout', {})
                .then(this.purgeUser)
                .then(() => router.push('sign-in'))
        },
    }
});

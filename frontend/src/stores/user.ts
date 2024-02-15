import {defineStore} from "pinia";
import router from "@/router";
import ApiService from "@/core/services/ApiService";

export const useUserStore = defineStore("user", {

    state() {
        return {
            user: {
                id: '',
                name: '',
                email: '',
                role: '',
            },
            roles: [],
            loading: false,
        }
    },

    actions: {
        getUser(userId) {
            this.loading = true;
            ApiService.post(`user/edit`, {userId})
                .then(response => {
                    this.user.id = response.data.id;
                    this.user.name = response.data.name;
                    this.user.email = response.data.email;
                    this.user.role = response.data.roles[0].id;
                })
                .finally(() => this.loading = false)
        },

        getRoles() {
            ApiService.post('roles', {})
                .then(response => this.roles = response.data)
        }

    }
});

<template>
  <!--begin::Tables Widget 11-->
  <div class="card" v-loading="loading">
    <!--begin::Header-->
    <div class="card-header border-0 pt-5">
      <h3 class="card-title align-items-start flex-column">
        <span class="card-label fw-bold fs-3 mb-1">Users</span>

        <span class="text-muted mt-1 fw-semibold fs-7"
        >{{ pagination.total }} registered users</span
        >
      </h3>
      <div class="card-toolbar">
        <a href="#" class="btn btn-sm btn-light-primary" @click="displayModal('new_user_modal')">
          <KTIcon icon-name="plus" icon-class="fs-2"/>
          New User
        </a>
      </div>
    </div>
    <!--end::Header-->

    <!--begin::Body-->
    <div class="card-body py-3">
      <!--begin::Table container-->
      <div class="table-responsive">
        <!--begin::Table-->
        <table class="table align-middle gs-0 gy-4">
          <!--begin::Table head-->
          <thead>
          <tr class="fw-bold text-muted bg-light">
            <th class="ps-4 min-w-325px rounded-start">Name</th>
            <th class="min-w-125px">Email</th>
            <th class="min-w-125px">Role</th>
            <th class="min-w-125px">Number of quote requests</th>
            <th class="min-w-200px text-end rounded-end"></th>
          </tr>
          </thead>
          <!--end::Table head-->

          <!--begin::Table body-->
          <tbody>
          <template v-for="(user, index) in users" :key="index">
            <tr>
              <td>
                <div class="d-flex align-items-center">
                  <div class="symbol symbol-50px me-5">
                    <img src="/media/avatars/blank.png" class="" alt=""/>
                  </div>

                  <div class="d-flex justify-content-start flex-column">
                    <a
                        href="#"
                        class="text-gray-900 fw-bold text-hover-primary mb-1 fs-6"
                    >{{ user.name }}</a
                    >
                  </div>
                </div>
              </td>

              <td>
                <a
                    class="text-gray-900 fw-bold text-hover-primary d-block mb-1 fs-6"
                >{{ user.email }}</a
                >
              </td>
              <td>
                <a class="text-gray-900 fw-bold text-hover-primary d-block mb-1 fs-6">
                  <span class="badge-light-success badge fs-7 fw-bold my-2" v-if="user?.roles[0]?.name === 'admin'">admin</span>
                  <span class="badge-light-info badge fs-7 fw-bold my-2" v-else>{{ user?.roles[0]?.name }}</span>
                </a>
              </td>

              <td>
                <a class="text-gray-900 fw-bold text-hover-primary mb-1 fs-6">{{ user.quote_requests_count }}</a>
                <span class="text-muted fw-semibold text-muted fs-7"> request</span>
              </td>

              <td class="text-end">
                <a
                    class="btn btn-icon btn-bg-light btn-active-color-primary btn-sm me-1"
                    @click="router.push({name:'edit-user', params:{id:user.id}})"
                >
                  <KTIcon icon-name="pencil" icon-class="fs-3"/>
                </a>

                <a
                    v-if="user.id !== authStore.getUser()?.id"
                    class="btn btn-icon btn-bg-light btn-active-color-primary btn-sm"
                    @click="deleteUser(user.id)"
                >
                  <KTIcon icon-name="trash" icon-class="fs-3"/>
                </a>
              </td>
            </tr>
          </template>
          </tbody>
          <!--end::Table body-->
        </table>
        <!--end::Table-->
      </div>
      <!--end::Table container-->
    </div>

    <el-pagination
        :current-page="pagination.currentPage"
        layout=" prev, pager, next"
        :total="pagination.total"
        :page-size="10"
        @current-change="getUsers"
    />
    <!--begin::Body-->
  </div>
  <NewUserModal @reloadUsers="getUsers"/>
</template>

<script lang="ts">
import {getAssetPath} from "@/core/helpers/assets";
import {defineComponent, onMounted, ref} from "vue";
import ApiService from "@/core/services/ApiService";
import {displayModal} from "@/core/helpers/modal";
import NewUserModal from "@/components/modals/user/NewUserModal.vue";
import {useAuthStore} from "@/stores/auth";
import Swal from "sweetalert2/dist/sweetalert2.js";
import router from "@/router";

export default defineComponent({
  name: "users",
  components: {NewUserModal},
  setup() {
    const users = ref([]);
    const loading = ref(false);
    const pagination = ref({
      currentPage: 1,
      total: 0
    });

    const getUsers = (page = 1) => {
      loading.value = true;
      ApiService.post('users', {page})
          .then(response => {
            users.value = response.data.data
            pagination.value.total = response.data.total
            pagination.value.currentPage = response.data.current_page
          })
          .finally(() => loading.value = false)
    }

    const deleteUser = userId => {
      Swal.fire({
        text: "Are you sure you want to delete user?",
        icon: "warning",
        confirmButtonText: "Yes",
        showDenyButton: true,
        denyButtonText: `No`,
        heightAuto: false,
      }).then(result => {

        if (result.isConfirmed) {
          loading.value = true;

          ApiService.post('user/delete', {userId})
              .then(getUsers)
              .finally(() => loading.value = false)
        }
      });


    }

    onMounted(getUsers)

    return {
      users,
      router,
      loading,
      getUsers,
      pagination,
      deleteUser,
      displayModal,
      getAssetPath,
      authStore: useAuthStore()
    };
  },
});
</script>

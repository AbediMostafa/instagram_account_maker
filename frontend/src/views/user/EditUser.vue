<template>
  <!--begin::details View-->
  <div class="card mb-5 mb-xl-10" id="kt_profile_details_view">
    <!--begin::Card header-->
    <div class="card-header cursor-pointer">
      <!--begin::Card title-->
      <div class="card-title m-0">
        <h3 class="fw-bold m-0">Profile Details</h3>
      </div>
    </div>
    <!--begin::Card header-->

    <!--begin::Card body-->
    <div class="card-body p-9">
      <el-form
          id="edit_user_modal_form"
          @submit.prevent="submit()"
          :model="user"
          :rules="rules"
          ref="formRef"
          class="form"
      >
        <!--begin::Row-->
        <div class="row mb-7">
          <!--begin::Label-->
          <label class="col-lg-2 fw-semibold text-muted">Name</label>
          <!--end::Label-->

          <!--begin::Col-->
          <div class="col-lg-6">
            <el-form-item prop="name">
              <el-input
                  v-model="user.name"
                  placeholder="Enter User's Name"
                  name="name"
              ></el-input>
            </el-form-item>
          </div>
          <!--end::Col-->
        </div>
        <div class="row mb-7">
          <!--begin::Label-->
          <label class="col-lg-2 fw-semibold text-muted">Email</label>
          <!--end::Label-->

          <!--begin::Col-->
          <div class="col-lg-6">
            <el-form-item prop="email">
              <el-input
                  v-model="user.email"
                  placeholder="Enter User's Email"
                  name="email"
              ></el-input>
            </el-form-item>
          </div>
          <!--end::Col-->
        </div>

        <div>
          <a class="btn btn-sm btn-success me-2" @click="displayModal('reset_password_modal')"> Reset Password</a>
          <!--begin::Button-->
          <button
              :data-kt-indicator="loading ? 'on' : null"
              class="btn btn-sm btn-primary"
              type="submit"
          >
                <span v-if="!loading" class="indicator-label">
                  Update
                </span>
            <span v-if="loading" class="indicator-progress">
                  Please wait...
                  <span
                      class="spinner-border spinner-border-sm align-middle ms-2"
                  ></span>
                </span>
          </button>
          <!--end::Button-->
        </div>

      </el-form>
    </div>
    <reset-password-modal/>

  </div>
</template>

<script lang="ts">
import {defineComponent, ref, watch} from "vue";
import {useUserStore} from "@/stores/user";
import ApiService from "@/core/services/ApiService";
import ResetPasswordModal from "@/components/modals/user/ResetPasswordModal.vue";
import {displayModal} from "@/core/helpers/modal";

export default defineComponent({
  name: "edit-user",
  methods: {displayModal},
  components: {ResetPasswordModal},
  setup() {
    const userStore = useUserStore();
    const formRef = ref<null | HTMLFormElement>(null);
    const user = ref({})
    const loading = ref(false)
    const rules = ref({
      name: [{required: true, message: "Please input name", trigger: "blur",}],
      email: [
        {type: 'email', message: 'Please input correct email address', trigger: ['blur', 'change']},
        {required: true, message: "Please input email address", trigger: "blur"}
      ],
    });

    watch(userStore.user, (o, n) => user.value = {...n})

    const submit = () => {
      if (!formRef.value)
        return;


      formRef.value.validate((valid: boolean) => {
        if (valid) {
          loading.value = true;

          ApiService.post('user/update', {...user.value})
              .finally(() => loading.value = false)

        } else {
          return false;
        }
      });
    };


    return {
      formRef,
      loading,
      submit,
      rules,
      user,
    };
  },
});
</script>

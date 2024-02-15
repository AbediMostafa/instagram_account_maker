<template>
  <!--begin::Modal - New Target-->
  <div
      class="modal fade"
      id="new_user_modal"
      ref="ruleFormRef"
      tabindex="-1"
      aria-hidden="true"
  >
    <!--begin::Modal dialog-->
    <div class="modal-dialog modal-dialog-centered mw-650px">
      <!--begin::Modal content-->
      <div class="modal-content rounded">
        <!--begin::Modal header-->
        <div class="modal-header pb-0 border-0 justify-content-end">
          <!--begin::Close-->
          <div
              class="btn btn-sm btn-icon btn-active-color-primary"
              data-bs-dismiss="modal"
          >
            <KTIcon icon-name="cross" icon-class="fs-1"/>
          </div>
          <!--end::Close-->
        </div>
        <!--begin::Modal header-->

        <!--begin::Modal body-->
        <div class="modal-body scroll-y px-10 px-lg-15 pt-0 pb-15">
          <!--begin:Form-->
          <el-form
              id="new_user_modal_form"
              @submit.prevent="submit()"
              :model="targetData"
              :rules="rules"
              ref="formRef"
              class="form"
          >
            <!--begin::Heading-->
            <div class="mb-13 text-center">
              <!--begin::Title-->
              <h1 class="mb-3">Add New User</h1>
              <!--end::Title-->

              <!--begin::Description-->
              <div class="text-gray-500 fw-semibold fs-5">
                please fill out all required fields
              </div>
              <!--end::Description-->
            </div>
            <!--end::Heading-->

            <!--begin::Input group-->
            <div class="row g-3 mb-4">
              <label class="required fs-6 fw-semibold">Name</label>
              <el-form-item prop="name">
                <el-input
                    v-model="targetData.name"
                    placeholder="Enter User's Name"
                    name="name"
                ></el-input>
              </el-form-item>
            </div>
            <!--end::Input group-->

            <!--begin::Input group-->
            <div class="row g-3 mb-4">
              <!--begin::Col-->
              <label class="required fs-6 fw-semibold mb-2">Role</label>
              <el-form-item prop="role" v-loading="is.rolesLoading">
                <el-select
                    v-model="targetData.role"
                    placeholder="Select a Role"
                    name="role"
                    as="select"
                >
                  <el-option value="">Select Role ...</el-option>
                  <el-option v-for="role in roles" :label="role.name" :value="role.id">{{ role.name }}</el-option>
                </el-select>
              </el-form-item>
            </div>
            <div class="row g-3 mb-4">
              <!--begin::Col-->
              <label class="required fs-6 fw-semibold mb-2">Email</label>

              <el-form-item prop="email">
                <el-input
                    v-model="targetData.email"
                    placeholder="Enter User's Email"
                    name="email"
                ></el-input>
              </el-form-item>
            </div>
            <div class="row g-3 mb-4">
              <label class="required fs-6 fw-semibold mb-2">Password</label>

              <el-form-item prop="password">
                <el-input
                    v-model="targetData.password"
                    placeholder="Enter a Password"
                    name="password"
                ></el-input>
              </el-form-item>
            </div>
            <div class="row g-3 mb-4">
              <label class="required fs-6 fw-semibold mb-2">Repeat Password</label>

              <el-form-item prop="repeatPassword">
                <el-input
                    v-model="targetData.repeatPassword"
                    placeholder="Confirm Password"
                    name="repeatPassword"
                ></el-input>
              </el-form-item>
            </div>
            <!--end::Input group-->

            <!--begin::Actions-->
            <div class="text-center">
              <button
                  type="reset"
                  id="new_user_modal_cancel"
                  data-bs-dismiss="modal"
                  class="btn btn-light me-3"
              >
                Cancel
              </button>

              <!--begin::Button-->
              <button
                  :data-kt-indicator="is.loading ? 'on' : null"
                  class="btn btn-lg btn-primary"
                  type="submit"
              >
                <span v-if="!is.loading" class="indicator-label">
                  Submit
                  <KTIcon icon-name="arrow-right" icon-class="fs-3 ms-2 me-0"/>
                </span>
                <span v-if="is.loading" class="indicator-progress">
                  Please wait...
                  <span
                      class="spinner-border spinner-border-sm align-middle ms-2"
                  ></span>
                </span>
              </button>
              <!--end::Button-->
            </div>
            <!--end::Actions-->
          </el-form>
          <!--end:Form-->
        </div>
        <!--end::Modal body-->
      </div>
      <!--end::Modal content-->
    </div>
    <!--end::Modal dialog-->
  </div>
  <!--end::Modal - New Target-->
</template>

<style lang="scss">
.el-select {
  width: 100%;
}

.el-date-editor.el-input,
.el-date-editor.el-input__inner {
  width: 100%;
}
</style>

<script lang="ts">
import {getAssetPath} from "@/core/helpers/assets";
import {defineComponent, onMounted, reactive, ref} from "vue";
import {hideModal} from "@/core/helpers/modal";
import Swal from "sweetalert2/dist/sweetalert2.js";
import ApiService from "@/core/services/ApiService";

export default defineComponent({
  name: "new-user-modal",
  components: {},
  setup(props, ctx) {
    const formRef = ref<null | HTMLFormElement>(null);
    const is = ref({
      loading: false,
      rolesLoading: false,
    })
    const ruleFormRef = ref();
    const roles = ref([]);
    const targetData = reactive({
      name: "",
      role: "",
      email: "",
      password: "",
      repeatPassword: "",
    });

    const validatePass = (rule: any, value: any, callback: any) => {
      if (value === '') {
        callback(new Error('Please input the password'))
      } else {
        callback()
      }
    }
    const validateRepeatPassword = (rule: any, value: any, callback: any) => {
      if (value === '') {
        callback(new Error('Please input the password again'))
      } else if (value !== targetData.password) {
        callback(new Error("Two inputs don't match!"))
      } else {
        callback()
      }
    }

    const rules = ref({
      name: [{required: true, message: "Please input name", trigger: "blur",}],
      email: [
        {type: 'email', message: 'Please input correct email address', trigger: ['blur', 'change']},
        {required: true, message: "Please input email address", trigger: "blur"}
      ],
      password: [{validator: validatePass, trigger: 'blur'}],
      repeatPassword: [{validator: validateRepeatPassword, trigger: ['blur', 'change']}],
    });

    const getRoles = () => {
      is.value.rolesLoading = true;
      ApiService.post('roles', {})
          .then(response => roles.value = response.data)
          .finally(() => is.value.rolesLoading = false)
    }

    onMounted(getRoles)

    const submit = () => {
      if (!formRef.value) {
        return;
      }

      formRef.value.validate((valid: boolean) => {
        if (valid) {
          is.value.loading = true;

          ApiService.post('user/create', {...targetData})
              .then(() => {
                ctx.emit('reloadUsers');
                formRef.value.resetFields();
                hideModal('new_user_modal');
              })
              .finally(() => {
                is.value.loading = false
              })

        } else {
          return false;
        }
      });
    };

    return {
      is,
      rules,
      roles,
      submit,
      formRef,
      targetData,
      ruleFormRef,
      getAssetPath,
    };
  },
});
</script>

<style lang="scss">
.override-styles {
  z-index: 99999 !important;
  pointer-events: initial;
}
</style>

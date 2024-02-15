<template>
  <div
      class="modal fade"
      id="reset_password_modal"
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
              id="reset_password_modal_form"
              @submit.prevent="submit()"
              :model="targetData"
              :rules="rules"
              ref="formRef"
              class="form"
          >
            <!--begin::Heading-->
            <div class="mb-13 text-center">
              <!--begin::Title-->
              <h1 class="mb-3">Reset Password</h1>
              <!--end::Title-->

              <!--begin::Description-->
              <div class="text-gray-500 fw-semibold fs-5">
                please fill out all required fields
              </div>
              <!--end::Description-->
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
                  id="reset_password_modal_cancel"
                  class="btn btn-light me-3"
                  data-bs-dismiss="modal"
              >
                Cancel
              </button>

              <button
                  :data-kt-indicator="loading ? 'on' : null"
                  class="btn btn-lg btn-primary"
                  type="submit"
              >
                <span v-if="!loading" class="indicator-label">
                  Submit
                  <KTIcon icon-name="arrow-right" icon-class="fs-3 ms-2 me-0"/>
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
import {defineComponent, reactive, ref, watch} from "vue";
import {hideModal} from "@/core/helpers/modal";
import ApiService from "@/core/services/ApiService";
import {useUserStore} from "@/stores/user";

export default defineComponent({
  name: "reset_password_modal",
  setup() {
    const formRef = ref<null | HTMLFormElement>(null);
    const loading = ref(false);
    const userId = ref('')
    const ruleFormRef = ref();
    const targetData = reactive({
      password: '',
      repeatPassword: '',
    })

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
      password: [{validator: validatePass, trigger: 'blur'}],
      repeatPassword: [{validator: validateRepeatPassword, trigger: ['blur', 'change']}],
    });

    watch(useUserStore().user, n => userId.value = n.id)


    const submit = () => {
      if (!formRef.value) {
        return;
      }

      formRef.value.validate((valid: boolean) => {
        if (valid) {
          loading.value = true;
          const data = {
            password:targetData.password,
            userId:userId.value
          }

          ApiService.post('user/reset-password', data)
              .then(() => {
                formRef.value.resetFields();
                hideModal('reset_password_modal');
              })
              .finally(() => {
                loading.value = false
              })

        } else {
          return false;
        }
      });
    };

    return {
      loading,
      rules,
      submit,
      formRef,
      targetData,
      ruleFormRef,
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

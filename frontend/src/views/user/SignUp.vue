<template>
  <!--begin::Wrapper-->
  <div class="w-lg-500px p-10">
    <!--begin::Form-->
    <VForm
        class="form w-100 fv-plugins-bootstrap5 fv-plugins-framework"
        @submit="onSubmitRegister"
        :validation-schema="registration"
    >
      <!--begin::Heading-->
      <div class="mb-10 text-center">
        <!--begin::Title-->
        <h1 class="text-gray-400 mb-3">Create an Account</h1>
        <!--end::Title-->

        <!--begin::Link-->
        <div class="text-gray-500 fw-semibold fs-4">
          Already have an account?

          <router-link to="/sign-in" class="link-primary fw-bold">
            Sign in here
          </router-link>
        </div>
        <!--end::Link-->
      </div>
      <!--end::Heading-->

      <!--begin::Action-->
      <!--end::Action-->

      <!--begin::Separator-->
      <div class="d-flex align-items-center mb-10">
        <div class="border-bottom border-gray-300 mw-50 w-100"></div>
        <span class="fw-semibold text-gray-400 fs-7 mx-2">OR</span>
        <div class="border-bottom border-gray-300 mw-50 w-100"></div>
      </div>
      <!--end::Separator-->

      <!--begin::Input group-->
      <div class="row fv-row mb-7">
        <!--begin::Col-->
        <div class="col-xl-12">
          <label class="form-label fw-bold text-gray-400 fs-6">Full Name</label>
          <Field
              class="form-control form-control-lg form-control-solid"
              type="text"
              placeholder=""
              name="name"
              autocomplete="off"
          />
          <div class="fv-plugins-message-container">
            <div class="fv-help-block">
              <ErrorMessage name="name"/>
            </div>
          </div>
        </div>
      </div>
      <!--end::Input group-->

      <!--begin::Input group-->
      <div class="fv-row mb-7">
        <label class="form-label fw-bold text-gray-400 fs-6">Email</label>
        <Field
            class="form-control form-control-lg form-control-solid"
            type="email"
            placeholder=""
            name="email"
            autocomplete="off"
        />
        <div class="fv-plugins-message-container">
          <div class="fv-help-block">
            <ErrorMessage name="email"/>
          </div>
        </div>
      </div>
      <!--end::Input group-->

      <!--begin::Input group-->
      <div class="mb-10 fv-row">
        <!--begin::Wrapper-->
        <div class="mb-1">
          <!--begin::Label-->
          <label class="form-label fw-bold text-gray-400 fs-6"> Password </label>
          <!--end::Label-->

          <!--begin::Input wrapper-->
          <div class="position-relative mb-3">
            <Field
                class="form-control form-control-lg form-control-solid"
                type="password"
                placeholder=""
                name="password"
                autocomplete="off"
            />
            <div class="fv-plugins-message-container">
              <div class="fv-help-block">
                <ErrorMessage name="password"/>
              </div>
            </div>
          </div>
          <!--end::Meter-->
        </div>
      </div>
      <!--end::Input group--->

      <!--begin::Input group-->
      <div class="fv-row mb-5">
        <label class="form-label fw-bold text-gray-400 fs-6"
        >Confirm Password</label
        >
        <Field
            class="form-control form-control-lg form-control-solid"
            type="password"
            placeholder=""
            name="password_confirmation"
            autocomplete="off"
        />
        <div class="fv-plugins-message-container">
          <div class="fv-help-block">
            <ErrorMessage name="password_confirmation"/>
          </div>
        </div>
      </div>
      <!--end::Input group-->

      <!--begin::Input group-->
      <div class="fv-row mb-10">
        <label class="form-check form-check-custom form-check-solid">
          <Field
              class="form-check-input"
              type="checkbox"
              name="toc"
              value="1"
          />
          <span class="form-check-label fw-semibold text-gray-700 fs-6">
            I Agree &
            <a href="#" class="ms-1 link-primary">Terms and conditions</a>.
          </span>
        </label>
      </div>
      <!--end::Input group-->

      <!--begin::Actions-->
      <div class="text-center">
        <button
            id="kt_sign_up_submit"
            ref="submitButton"
            type="submit"
            class="btn btn-lg btn-primary"
        >
          <span class="indicator-label"> Submit </span>
          <span class="indicator-progress">
            Please wait...
            <span
                class="spinner-border spinner-border-sm align-middle ms-2"
            ></span>
          </span>
        </button>
      </div>
      <!--end::Actions-->
    </VForm>
    <!--end::Form-->
  </div>
  <!--end::Wrapper-->
</template>

<script lang="ts">
import {getAssetPath} from "@/core/helpers/assets";
import {defineComponent, nextTick, onMounted, ref} from "vue";
import {ErrorMessage, Field, Form as VForm} from "vee-validate";
import * as Yup from "yup";
import {useAuthStore, type User} from "@/stores/auth";
import {useRouter} from "vue-router";
import {PasswordMeterComponent} from "@/assets/ts/components";
import Swal from "sweetalert2/dist/sweetalert2.js";
import ApiService from "@/core/services/ApiService";
import router from "@/router";

export default defineComponent({
  name: "sign-up",
  components: {
    Field,
    VForm,
    ErrorMessage,
  },
  setup() {
    const store = useAuthStore();
    const router = useRouter();

    const submitButton = ref<HTMLButtonElement | null>(null);

    const registration = Yup.object().shape({
      name: Yup.string().required().label("Name"),
      email: Yup.string().min(4).required().email().label("Email"),
      password: Yup.string().required().label("Password"),
      password_confirmation: Yup.string()
          .required()
          .oneOf([Yup.ref("password")], "Passwords must match")
          .label("Password Confirmation"),
    });


    const onSubmitRegister = (values: any) => {
      console.log(values)
      activateButton()
      ApiService.post('signup', values)
          .then(response => {

            if (response.data.status) {
              store.setUser(response.data.user)
              router.push('dashboard');
            }
          })
          .finally(deactivateButton)
    };

    const activateButton = () => {
      if (submitButton.value) {
        // eslint-disable-next-line
        submitButton.value!.disabled = true;
        // Activate indicator
        submitButton.value.setAttribute("data-kt-indicator", "on");
      }
    }

    const deactivateButton = () => {
      submitButton.value?.removeAttribute("data-kt-indicator");
      // eslint-disable-next-line
      submitButton.value!.disabled = false;
    }

    return {
      registration,
      onSubmitRegister,
      submitButton,
      getAssetPath,
    };
  },
});
</script>

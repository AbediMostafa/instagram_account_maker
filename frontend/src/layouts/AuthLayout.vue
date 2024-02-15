<template>
  <!--begin::Authentication Layout -->
  <div class="d-flex flex-column flex-lg-row flex-column-fluid" style="background-image: url(/media/auth/bg10-dark.jpeg);">
    <!--begin::Body-->
    <div
      class="d-flex flex-column flex-lg-row-fluid w-lg-50 p-10 order-2 order-lg-1"
    >
      <!--begin::Form-->
      <div class="d-flex flex-center flex-column flex-lg-row-fluid">
        <!--begin::Wrapper-->
        <div class="w-lg-500px p-10">
          <router-view></router-view>
        </div>
        <!--end::Wrapper-->
      </div>
      <!--end::Form-->

      <!--begin::Footer-->
      <div class="d-flex flex-center flex-wrap px-5">
        <!--begin::Links-->
        <div class="d-flex fw-semibold text-primary fs-base">
          <a href="#" class="px-5" target="_blank">Terms</a>

          <a href="#" class="px-5" target="_blank">Plans</a>

          <a href="#" class="px-5" target="_blank">Contact Us</a>
        </div>
        <!--end::Links-->
      </div>
      <!--end::Footer-->
    </div>
    <!--end::Body-->

    <!--begin::Aside-->
    <div
      class="d-flex flex-lg-row-fluid w-lg-50 bgi-size-cover bgi-position-center order-1 order-lg-2"
      :style="`background-image: url('${getAssetPath(
        '/media/misc/auth-bg.png'
      )}')`"
    >
      <!--begin::Content-->
      <div
        class="d-flex flex-column flex-center py-7 py-lg-15 px-5 px-md-15 w-100"
      >
        <!--begin::Image-->
        <img
          class="d-none d-lg-block mx-auto w-275px w-md-50 mb-10 mb-lg-20"
          :src="getAssetPath('media/auth/agency.png')"
          alt=""
        />
        <!--end::Image-->

        <!--begin::Title-->
        <h1
          class="d-none d-lg-block text-white fs-2qx fw-bolder text-center mb-7"
        >
          Fast, Efficient and Productive
        </h1>
        <!--end::Title-->

        <!--begin::Text-->
        <div class="d-none d-lg-block text-white fs-base text-center">

          With this application, you can automate the registration of
          <a class="opacity-75-hover text-warning fw-bold me-1">Instagram</a>
          accounts. It is a simple process that uses phone numbers to register and create accounts. Please ensure you perform the

          <a class="opacity-75-hover text-warning fw-bold me-1">humanation</a>
          process on the accounts to keep them active.
        </div>
        <!--end::Text-->
      </div>
      <!--end::Content-->
    </div>
    <!--end::Aside-->
  </div>
  <!--end::Authentication Layout -->
</template>

<script lang="ts">
import { getAssetPath } from "@/core/helpers/assets";
import { defineComponent, onMounted } from "vue";
import LayoutService from "@/core/services/LayoutService";
import { useBodyStore } from "@/stores/body";

export default defineComponent({
  name: "auth-layout",
  components: {},
  setup() {
    const store = useBodyStore();

    onMounted(() => {
      LayoutService.emptyElementClassesAndAttributes(document.body);

      store.addBodyClassname("app-blank");
      store.addBodyClassname("bg-body");
    });

    return {
      getAssetPath,
    };
  },
});
</script>

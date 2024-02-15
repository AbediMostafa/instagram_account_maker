<template>
  <!--begin::Card-->
  <div
    class="card card-flush mb-0"
    id="kt_view_summary"
    data-kt-sticky="true"
    data-kt-sticky-name="view-subscription-summary"
    data-kt-sticky-offset="{default: false, lg: '200px'}"
    data-kt-sticky-width="{lg: '250px', xl: '300px'}"
    data-kt-sticky-left="auto"
    data-kt-sticky-top="150px"
    data-kt-sticky-animation="false"
    data-kt-sticky-zindex="95"
  >
    <!--begin::Card header-->
    <div class="card-header">
      <!--begin::Card title-->
      <div class="card-title">
        <h2>Summary</h2>
      </div>
      <!--end::Card title-->

      <!--begin::Card toolbar-->
      <div class="card-toolbar">
        <!--begin::More options-->
        <a
          href="#"
          class="btn btn-sm btn-light btn-icon"
          data-kt-menu-trigger="click"
          data-kt-menu-placement="bottom-end"
        >
          <KTIcon icon-name="dots-horizontal" icon-class="fs-3" />
        </a>
        <UserMenu></UserMenu>
        <!--end::More options-->
      </div>
      <!--end::Card toolbar-->
    </div>
    <!--end::Card header-->

    <!--begin::Card body-->
    <div class="card-body pt-0 fs-6">
      <!--begin::Section-->
      <div class="mb-7">
        <!--begin::Details-->
        <div class="d-flex align-items-center">
          <!--begin::Avatar-->
          <div class="symbol symbol-60px symbol-circle me-3">
            <img alt="Pic" :src="getAssetPath('media/avatars/blank.png')" />
          </div>
          <!--end::Avatar-->

          <!--begin::Info-->
          <div class="d-flex flex-column">
            <!--begin::Name-->
            <a
              class="fs-4 fw-bold text-gray-900 text-hover-primary me-2"
              >{{ quote.user?.name }}</a
            >
            <!--end::Name-->

            <!--begin::Email-->
            <a href="#" class="fw-semibold text-gray-600 text-hover-primary"
              >{{ quote.user?.email }}</a
            >
            <!--end::Email-->
          </div>
          <!--end::Info-->
        </div>
        <!--end::Details-->
      </div>
      <!--end::Section-->

      <!--begin::Seperator-->
      <div class="separator separator-dashed mb-7"></div>
      <!--end::Seperator-->

      <!--begin::Section-->
      <div class="mb-7">
        <!--begin::Title-->
        <h5 class="mb-4">Product details</h5>
        <!--end::Title-->

        <!--begin::Details-->
        <div class="mb-0">
          <!--begin::Plan-->
          <span class="badge badge-light-info me-2">Total</span>
          <!--end::Plan-->

          <!--begin::Price-->
          <span class="fw-semibold text-gray-600">$149.99 / Year</span>
          <!--end::Price-->
        </div>
        <!--end::Details-->
      </div>
      <!--end::Section-->

      <!--begin::Seperator-->
      <div class="separator separator-dashed mb-7"></div>
      <!--end::Seperator-->

      <!--begin::Section-->
<!--      <div class="mb-10">-->
<!--        &lt;!&ndash;begin::Title&ndash;&gt;-->
<!--        <h5 class="mb-4">Payment Details</h5>-->
<!--        &lt;!&ndash;end::Title&ndash;&gt;-->

<!--        &lt;!&ndash;begin::Details&ndash;&gt;-->
<!--        <div class="mb-0">-->
<!--          &lt;!&ndash;begin::Card info&ndash;&gt;-->
<!--          <div class="fw-semibold text-gray-600 d-flex align-items-center">-->
<!--            Mastercard-->

<!--            <img-->
<!--              :src="getAssetPath('media/svg/card-logos/mastercard.svg')"-->
<!--              class="w-35px ms-2"-->
<!--              alt=""-->
<!--            />-->
<!--          </div>-->
<!--          &lt;!&ndash;end::Card info&ndash;&gt;-->

<!--          &lt;!&ndash;begin::Card expiry&ndash;&gt;-->
<!--          <div class="fw-semibold text-gray-600">Expires Dec 2024</div>-->
<!--          &lt;!&ndash;end::Card expiry&ndash;&gt;-->
<!--        </div>-->
<!--        &lt;!&ndash;end::Details&ndash;&gt;-->
<!--      </div>-->
      <!--end::Section-->

      <!--begin::Seperator-->
<!--      <div class="separator separator-dashed mb-7"></div>-->
      <!--end::Seperator-->

      <!--begin::Section-->
<!--      <div class="mb-10">-->
<!--        &lt;!&ndash;begin::Title&ndash;&gt;-->
<!--        <h5 class="mb-4">Subscription Details</h5>-->
<!--        &lt;!&ndash;end::Title&ndash;&gt;-->

<!--        &lt;!&ndash;begin::Details&ndash;&gt;-->
<!--        <table class="table fs-6 fw-semibold gs-0 gy-2 gx-2">-->
<!--          &lt;!&ndash;begin::Row&ndash;&gt;-->
<!--          <tr class="">-->
<!--            <td class="text-gray-500">Subscription ID:</td>-->
<!--            <td class="text-gray-800">sub_4567_8765</td>-->
<!--          </tr>-->
<!--          &lt;!&ndash;end::Row&ndash;&gt;-->

<!--          &lt;!&ndash;begin::Row&ndash;&gt;-->
<!--          <tr class="">-->
<!--            <td class="text-gray-500">Started:</td>-->
<!--            <td class="text-gray-800">15 Apr 2021</td>-->
<!--          </tr>-->
<!--          &lt;!&ndash;end::Row&ndash;&gt;-->

<!--          &lt;!&ndash;begin::Row&ndash;&gt;-->
<!--          <tr class="">-->
<!--            <td class="text-gray-500">Status:</td>-->
<!--            <td><span class="badge badge-light-success">Active</span></td>-->
<!--          </tr>-->
<!--          &lt;!&ndash;end::Row&ndash;&gt;-->

<!--          &lt;!&ndash;begin::Row&ndash;&gt;-->
<!--          <tr class="">-->
<!--            <td class="text-gray-500">Next Invoice:</td>-->
<!--            <td class="text-gray-800">15 Apr 2022</td>-->
<!--          </tr>-->
<!--          &lt;!&ndash;end::Row&ndash;&gt;-->
<!--        </table>-->
<!--        &lt;!&ndash;end::Details&ndash;&gt;-->
<!--      </div>-->
      <!--end::Section-->

      <!--begin::Actions-->
      <div class="mb-0 d-flex">
        <router-link
          :to="{name:'quotes'}"
          class="btn btn-primary btn-sm"
          id="kt_subscriptions_create_button"
        >
          Edit Subscription
        </router-link>
        <router-link
            :to="{name:'quotes'}"
            class="btn btn-light-primary btn-sm ms-2"
            id="kt_subscriptions_create_button"
        >
          quotes
        </router-link>
      </div>
      <!--end::Actions-->
    </div>
    <!--end::Card body-->
  </div>
  <!--end::Card-->
</template>

<script lang="ts">
import { getAssetPath } from "@/core/helpers/assets";
import { defineComponent } from "vue";
import UserMenu from "@/layouts/default-layout/components/menus/UserAccountMenu.vue";

export default defineComponent({
  name: "kt-summary",
  components: {
    UserMenu,
  },
  props:["quote"],
  setup() {
    return {
      getAssetPath,
    };
  },
});
</script>

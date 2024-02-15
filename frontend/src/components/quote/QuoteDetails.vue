<template>
  <!--begin::Card-->
  <div class="card card-flush pt-3 mb-5 mb-xl-10">
    <!--begin::Card header-->
    <div class="card-header">
      <!--begin::Card title-->
      <div class="card-title">
        <h2 class="fw-bold">Quote Details</h2>
      </div>
      <!--begin::Card title-->

      <!--begin::Card toolbar-->
      <div class="card-toolbar">
        <router-link to="" class="btn btn-light-primary"
        >Approve Quote
        </router-link
        >
      </div>
      <!--end::Card toolbar-->
    </div>
    <!--end::Card header-->

    <!--begin::Card body-->
    <div class="card-body pt-3">
      <!--begin::Section-->
      <div class="mb-10">
        <!--begin::Title-->
<!--        <h5 class="mb-4">Quote Imformation:</h5>-->
        <!--end::Title-->

        <!--begin::Details-->
        <div class="d-flex flex-wrap py-5">
          <!--begin::Row-->
          <div class="flex-equal me-5">
            <!--begin::Details-->
            <table class="table fs-6 fw-semibold gs-0 gy-2 gx-2 m-0">
              <!--begin::Row-->
              <tr>
                <td class="text-gray-500 min-w-200px w-200px">Bill to:</td>
                <td class="text-gray-800 min-w-200px">
                  {{ quote.user?.email }}
                </td>
              </tr>
              <!--end::Row-->

              <!--begin::Row-->
              <tr>
                <td class="text-gray-500">Customer Name:</td>
                <td class="text-gray-800">Emma Smith</td>
              </tr>
              <!--end::Row-->

              <!--begin::Row-->
              <tr>
                <td class="text-gray-500">Address:</td>
                <td class="text-gray-800">{{ quote.address }}</td>
              </tr>
              <!--end::Row-->

              <!--begin::Row-->
              <tr>
                <td class="text-gray-500">Number of stumps:</td>
                <td class="text-gray-800">{{ quote.number_of_stumps }}</td>
              </tr>
              <!--end::Row-->
            </table>
            <!--end::Details-->
          </div>
          <!--end::Row-->

          <!--begin::Row-->
          <div class="flex-equal">
            <!--begin::Details-->
            <table class="table fs-6 fw-semibold gs-0 gy-2 gx-2 m-0">
              <!--begin::Row-->
              <tr>
                <td class="text-gray-500 min-w-200px w-200px">
                  Largest tree :
                </td>
                <td class="text-gray-800 min-w-200px">
                  {{ quote.diameter_of_largest_tree }}
                </td>
              </tr>
              <!--end::Row-->

              <!--begin::Row-->
              <tr>
                <td class="text-gray-500">Area:</td>
                <td class="text-gray-800">{{ quote.area }}</td>
              </tr>
              <!--end::Row-->

              <!--begin::Row-->
              <tr>
                <td class="text-gray-500">Stump high less than 1 ft:</td>
                <td>
                  <span
                      style="color: var(--bs-success)!important;
                      background-color: var(--bs-success-light);!important;"
                      class="badge badge-light-success me-2" v-if="quote.current_stump_high_is_less_than_12">YES</span>
                  <span class="badge badge-light-danger me-2" v-else>NO</span>
                </td>
              </tr>
              <!--end::Row-->

              <!--begin::Row-->
              <tr>
                <td class="text-gray-500">Creation date:</td>
                <td class="text-gray-800">{{ quote.created_at }}</td>
              </tr>
              <!--end::Row-->
            </table>
            <!--end::Details-->
          </div>
          <!--end::Row-->
        </div>
        <!--end::Row-->
      </div>
      <!--end::Section-->

      <!--begin::Section-->
<!--      <div class="mb-0">-->
<!--        &lt;!&ndash;begin::Title&ndash;&gt;-->
<!--        <h5 class="mb-4">Subscribed Products:</h5>-->
<!--        &lt;!&ndash;end::Title&ndash;&gt;-->

<!--        &lt;!&ndash;begin::Product table&ndash;&gt;-->
<!--        <div class="table-responsive">-->
<!--          &lt;!&ndash;begin::Table&ndash;&gt;-->
<!--          <table class="table align-middle table-row-dashed fs-6 gy-4 mb-0">-->
<!--            &lt;!&ndash;begin::Table head&ndash;&gt;-->
<!--            <thead>-->
<!--            &lt;!&ndash;begin::Table row&ndash;&gt;-->
<!--            <tr-->
<!--                class="border-bottom border-gray-200 text-start text-gray-500 fw-bold fs-7 text-uppercase gs-0"-->
<!--            >-->
<!--              <th class="min-w-150px">Product</th>-->
<!--              <th class="min-w-125px">Subscription ID</th>-->
<!--              <th class="min-w-125px">Qty</th>-->
<!--              <th class="min-w-125px">Total</th>-->
<!--              <th class="text-end min-w-70px">Actions</th>-->
<!--            </tr>-->
<!--            &lt;!&ndash;end::Table row&ndash;&gt;-->
<!--            </thead>-->
<!--            &lt;!&ndash;end::Table head&ndash;&gt;-->

<!--            &lt;!&ndash;begin::Table body&ndash;&gt;-->
<!--            <tbody class="fw-semibold text-gray-800">-->
<!--            <tr>-->
<!--              <td>-->
<!--                <label class="w-150px">Basic Bundle</label>-->
<!--                <div class="fw-normal text-gray-600">Basic yearly bundle</div>-->
<!--              </td>-->
<!--              <td>-->
<!--                <span class="badge badge-light-danger">sub_4567_8765</span>-->
<!--              </td>-->
<!--              <td>1</td>-->
<!--              <td>$149.99 / Year</td>-->
<!--              <td class="text-end">-->
<!--                &lt;!&ndash;begin::Action&ndash;&gt;-->
<!--                <a-->
<!--                    href="#"-->
<!--                    class="btn btn-icon btn-active-light-primary w-30px h-30px"-->
<!--                    data-kt-menu-trigger="click"-->
<!--                    data-kt-menu-placement="bottom-end"-->
<!--                >-->
<!--                  <KTIcon icon-name="switch" icon-class="fs-3"/>-->
<!--                </a>-->
<!--                <UserMenu></UserMenu>-->
<!--                &lt;!&ndash;end::Action&ndash;&gt;-->
<!--              </td>-->
<!--            </tr>-->
<!--            <tr>-->
<!--              <td>-->
<!--                <label class="w-150px">Pro Bundle</label>-->
<!--                <div class="fw-normal text-gray-500">Basic yearly bundle</div>-->
<!--              </td>-->
<!--              <td>-->
<!--                <span class="badge badge-light-danger">sub_4567_3433</span>-->
<!--              </td>-->
<!--              <td>5</td>-->
<!--              <td>$949.99 / Year</td>-->
<!--              <td class="text-end">-->
<!--                &lt;!&ndash;begin::Action&ndash;&gt;-->
<!--                <a-->
<!--                    href="#"-->
<!--                    class="btn btn-icon btn-active-light-primary w-30px h-30px"-->
<!--                    data-kt-menu-trigger="click"-->
<!--                    data-kt-menu-placement="bottom-end"-->
<!--                >-->
<!--                  <KTIcon icon-name="switch" icon-class="fs-3"/>-->
<!--                </a>-->
<!--                <UserMenu></UserMenu>-->
<!--                &lt;!&ndash;end::Action&ndash;&gt;-->
<!--              </td>-->
<!--            </tr>-->
<!--            </tbody>-->
<!--            &lt;!&ndash;end::Table body&ndash;&gt;-->
<!--          </table>-->
<!--          &lt;!&ndash;end::Table&ndash;&gt;-->
<!--        </div>-->
<!--        &lt;!&ndash;end::Product table&ndash;&gt;-->
<!--      </div>-->
      <!--end::Section-->
    </div>
    <!--end::Card body-->
  </div>
  <!--end::Card-->
</template>

<script lang="ts">
import {getAssetPath} from "@/core/helpers/assets";
import {defineComponent} from "vue";
import UserMenu from "@/layouts/default-layout/components/menus/UserAccountMenu.vue";

export default defineComponent({
  name: "kt-details",
  components: {
    UserMenu,
  },
  props: ['quote'],
  setup() {

    return {
      getAssetPath,
    };
  },
});
</script>

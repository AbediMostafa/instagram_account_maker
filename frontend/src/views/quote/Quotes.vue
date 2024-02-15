<template>
  <!--begin::Tables Widget 11-->
  <div class="card" v-loading="loading">
    <!--begin::Header-->
    <div class="card-header border-0 pt-5">
      <h3 class="card-title align-items-start flex-column">
        <span class="card-label fw-bold fs-3 mb-1">Quotes</span>

        <span class="text-muted mt-1 fw-semibold fs-7"
        >{{ pagination.total }} requested quotes</span
        >
      </h3>
      <div class="card-toolbar">
        <a href="#" class="btn btn-sm btn-light-primary" @click="displayModal('new_quote_modal')">
          <KTIcon icon-name="plus" icon-class="fs-2"/>
          New Quote Request
        </a>
      </div>
    </div>
    <!--end::Header-->

    <!--begin::Body-->
    <div class="card-body py-3">
      <!--begin::Table container-->
      <div class="table-responsive">
        <!--begin::Table-->
        <table v-if="pagination.total" class="table align-middle gs-0 gy-4">
          <!--begin::Table head-->
          <thead>
          <tr class="fw-bold text-muted bg-light">
            <th class="ps-4 min-w-150px rounded-start">Number Of Stumps</th>
            <th class="min-w-125px">Diameter Of Largest</th>
            <th class="min-w-225px">Area</th>
            <th class="min-w-125px">Stump Position</th>
            <th class="min-w-80px">Less than 12</th>
            <th class="min-w-100px">User</th>
            <th class="min-w-150px text-end rounded-end"></th>
          </tr>
          </thead>
          <!--end::Table head-->

          <!--begin::Table body-->
          <tbody>
          <template v-for="(quote, index) in quotes" :key="index">
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
                    >{{ quote.number_of_stumps }}</a
                    >
                  </div>
                </div>
              </td>

              <td>
                <a
                    class="text-gray-900 fw-bold text-hover-primary d-block mb-1 fs-6"
                >{{ quote.diameter_of_largest_tree }}</a
                >
              </td>
              <td>
                <a
                    class="text-gray-900 fw-bold text-hover-primary d-block mb-1 fs-6"
                >{{ quote.area }}</a
                >
              </td>
              <td>
                <a
                    class="text-gray-900 fw-bold text-hover-primary d-block mb-1 fs-6"
                >{{ quote.stump_position }}</a
                >
              </td>
              <td>
                <a class="text-gray-900 fw-bold text-hover-primary d-block mb-1 fs-6">
                  <span class="badge-light-success badge fs-7 fw-bold my-2"
                        v-if="quote?.current_stump_high_is_less_than_12">yes</span>
                  <span class="badge-light-info badge fs-7 fw-bold my-2" v-else>no</span>
                </a>
              </td>

              <td>
                <a class="text-gray-900 fw-bold text-hover-primary mb-1 fs-6 d-block">{{ quote.user?.name }}</a>
                <span class="text-muted fw-semibold text-muted fs-7 d-block"> {{ quote.user?.email }}</span>
              </td>

              <td class="text-end">
                <router-link
                    :to="{name:'quote', params:{id:quote.id}}"
                    class="btn btn-icon btn-bg-light btn-active-color-primary btn-sm me-1"
                >
                  <KTIcon icon-name="eye" icon-class="fs-3"/>
                </router-link>
                <a
                    class="btn btn-icon btn-bg-light btn-active-color-primary btn-sm"
                    @click="deleteQuote(quote.id)"
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
        <div v-else class="text-center">
          <h1 class="mt-10 text-gray-700 fs-2hx">No quotes yet</h1>

          <img
              class="mw-300 mh-500px theme-light-show"
              src="/media/empty.jpg" alt=""/>


        </div>
      </div>
      <!--end::Table container-->
    </div>
    <el-pagination
        :current-page="pagination.currentPage"
        layout=" prev, pager, next"
        :total="pagination.total"
        :page-size="10"
        @current-change="getQuotes"
    />
    <!--begin::Body-->
  </div>
  <new-quote-modal @reloadQuotes="getQuotes"/>
</template>

<script lang="ts">
import {getAssetPath} from "@/core/helpers/assets";
import {defineComponent, onMounted, ref} from "vue";
import ApiService from "@/core/services/ApiService";
import {displayModal} from "@/core/helpers/modal";
import NewQuoteModal from "@/components/modals/quote/NewQuoteModal.vue";
import Swal from "sweetalert2/dist/sweetalert2.js";
import router from "@/router";

export default defineComponent({
  name: "quotes",
  components: {
    NewQuoteModal,
  },
  setup() {
    const quotes = ref([]);
    const loading = ref(false);
    const pagination = ref({
      currentPage: 1,
      total: 0
    });

    const getQuotes = (page = 1) => {
      loading.value = true;
      ApiService.post('quotes', {page})
          .then(response => {
            quotes.value = response.data.data
            pagination.value.total = response.data.total
            pagination.value.currentPage = response.data.current_page
          })
          .finally(() => loading.value = false)
    }

    const deleteQuote = quoteId => {
      Swal.fire({
        text: "Are you sure you want to delete quote request?",
        icon: "warning",
        confirmButtonText: "Yes",
        showDenyButton: true,
        denyButtonText: `No`,
        heightAuto: false,
      }).then(result => {

        if (result.isConfirmed) {
          loading.value = true;
          console.log(quoteId)

          ApiService.post('quote/delete', {quoteId})
              .then(getQuotes)
              .finally(() => loading.value = false)
        }
      });
    }

    onMounted(getQuotes)

    return {
      quotes,
      router,
      loading,
      getQuotes,
      pagination,
      deleteQuote,
      displayModal,
      getAssetPath,
    };
  },
});
</script>

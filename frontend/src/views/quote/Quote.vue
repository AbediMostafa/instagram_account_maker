<template>
  <!--begin::Layout-->
  <div class="d-flex flex-column flex-lg-row">
    <!--begin::Content-->
    <div class="flex-lg-row-fluid me-lg-15 order-2 order-lg-1 mb-10 mb-lg-0">
      <QuoteDetails :quote="quote" v-loading="loading"></QuoteDetails>

      <quote-invoice></quote-invoice>
    </div>
    <!--end::Content-->

    <!--begin::Sidebar-->
    <div
        class="flex-column flex-lg-row-auto w-lg-250px w-xl-300px mb-10 order-1 order-lg-2"
    >
      <QuoteSummary :quote="quote" v-loading="loading"></QuoteSummary>
    </div>
    <!--end::Sidebar-->
  </div>
  <!--end::Layout-->
</template>

<script lang="ts">
import {defineComponent, onMounted, ref} from "vue";
import QuoteDetails from "@/components/quote/QuoteDetails.vue";
import Invoices from "@/components/subscriptions/view/Invoices.vue";
import ApiService from "@/core/services/ApiService";
import QuoteSummary from "@/components/quote/QuoteSummary.vue";
import QuoteInvoice from "@/components/quote/QuoteInvoice.vue";

export default defineComponent({
  name: "kt-view-subscription",
  components: {
    QuoteInvoice,
    Invoices,
    QuoteDetails,
    QuoteSummary
  },
  props: ['id'],
  setup(props) {
    const quote = ref({});
    const loading = ref(false);

    const getQuote = () => {
      loading.value = true;
      ApiService.post('quote/show', {quoteId: props.id})
          .then(response => quote.value = response.data)
          .then(console.log)
          .finally(()=>loading.value = false)
    }

    onMounted(getQuote)

    return {
      quote,
      loading,
    }

  }
});
</script>

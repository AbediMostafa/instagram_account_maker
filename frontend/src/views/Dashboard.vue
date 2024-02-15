<template>
  <!--begin::Row-->
  <div class="card">
    <!--begin::Col-->
    <div class="card-body py-3 my-4">
      <new-quote @reloadQuotes="router.push('quotes')"/>
    </div>
  </div>
  <!--end::Row-->
</template>

<script lang="ts">
import {getAssetPath} from "@/core/helpers/assets";
import {defineComponent} from "vue";
import NewQuote from "@/components/quote/NewQuote.vue";
import router from "@/router";

export default defineComponent({
  name: "main-dashboard",
  methods: {},
  components: {
    NewQuote,
  },
  setup() {

    return {
      getAssetPath,
      router,
    };
  },
});
</script>

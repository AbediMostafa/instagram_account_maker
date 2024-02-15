<template>
  <div >
    <el-form
        id="new_quote_modal_form"
        @submit.prevent="submit()"
        :model="targetData"
        :rules="rules"
        ref="formRef"
        class="form"
    >
      <!--begin::Heading-->
      <div class="mb-13 text-center">
        <!--begin::Title-->
        <h1 class="mb-3">Get A Free Quote Now</h1>
        <!--end::Title-->

        <!--begin::Description-->
        <div class="text-gray-500 fw-semibold fs-5">
          The Stump PRO
        </div>
        <!--end::Description-->
      </div>
      <!--end::Heading-->

      <!--begin::Input group-->
      <div class="row g-3 mb-4">
        <label class="required fs-6 fw-semibold">Address</label>
        <el-form-item prop="address">
          <el-input
              v-model="targetData.address"
              placeholder="Enter Your Address"
              name="address"
          ></el-input>
        </el-form-item>
      </div>
      <div class="row g-3 mb-4">
        <!--begin::Col-->
        <label class="required fs-6 fw-semibold mb-2">How many stumps do you need removed</label>
        <el-form-item prop="number_of_stumps">
          <el-select
              v-model="targetData.number_of_stumps"
              placeholder="Number of stumps"
              name="number_of_stumps"
              as="select"
          >
            <el-option value="">Number of stumps ...</el-option>
            <el-option v-for="number in apis.number_of_stumps" :label="number" :value="number">{{
                number
              }}
            </el-option>
          </el-select>
        </el-form-item>
      </div>
      <div class="row g-3 mb-4">
        <!--begin::Col-->
        <label class="required fs-6 fw-semibold mb-2">What is the diameter of largest tree stump</label>
        <el-form-item prop="diameter_of_largest_tree">
          <el-select
              v-model="targetData.diameter_of_largest_tree"
              placeholder="Diameter of largest tree"
              name="diameter_of_largest_tree"
              as="select"
          >
            <el-option value="">Diameter of largest tree ...</el-option>
            <el-option v-for="number in apis.diameter_of_largest_tree" :label="number" :value="number">{{
                number
              }}
            </el-option>
          </el-select>
        </el-form-item>
      </div>
      <div class="row g-3 mb-4">
        <!--begin::Col-->
        <label class="required fs-6 fw-semibold mb-2">What would you like to do with the area </label>
        <el-form-item prop="area">
          <el-select
              v-model="targetData.area"
              placeholder="area"
              name="area"
              as="select"
          >
            <el-option value="">Area ...</el-option>
            <el-option v-for="number in apis.area" :label="number" :value="number">{{ number }}</el-option>
          </el-select>
        </el-form-item>
      </div>
      <div class="row g-3 mb-4">
        <!--begin::Col-->
        <label class="required fs-6 fw-semibold mb-2">Is the current stump less than 12" high?</label>
        <el-form-item prop="current_stump_high_is_less_than_12">
          <el-select
              v-model="targetData.current_stump_high_is_less_than_12"
              placeholder="Is the current stump less than 12 high?"
              name="current_stump_high_is_less_than_12"
              as="select"
          >
            <el-option value="">Is less than 12" high? ...</el-option>
            <el-option label="yes" :value="1">Yes</el-option>
            <el-option label="no" :value="0">No</el-option>
          </el-select>
        </el-form-item>
      </div>
      <div class="row g-3 mb-4">
        <!--begin::Col-->
        <label class="required fs-6 fw-semibold mb-2">Is the stump in front or backyard?</label>
        <el-form-item prop="stump_position">
          <el-select
              v-model="targetData.stump_position"
              placeholder="Stump position"
              name="stump_position"
              as="select"
          >
            <el-option value="">Stump position ...</el-option>
            <el-option v-for="stumpPosition in apis.stump_position" :label="stumpPosition" :value="stumpPosition">
              {{ stumpPosition }}
            </el-option>
          </el-select>
        </el-form-item>
      </div>
      <div class="text-center">
        <!--begin::Button-->
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
      </div>
    </el-form>
  </div>
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
    const loading = ref(false);
    const ruleFormRef = ref();
    const apis = ref({});
    const targetData = reactive({
      address: "",
      number_of_stumps: "",
      diameter_of_largest_tree: "",
      area: "",
      stump_position: "",
      current_stump_high_is_less_than_12: "",
    });

    const rules = ref({
      address: [{required: true, message: "Please input address", trigger: "blur",}],
      number_of_stumps: [{required: true, message: "Please select a number", trigger: ['blur', 'change'],}],
      diameter_of_largest_tree: [{
        required: true,
        message: "Please specify size of largest tree",
        trigger: ['blur', 'change'],
      }],
      area: [{required: true, message: "What would you like to do with the area? ", trigger: ['blur', 'change'],}],
      stump_position: [{required: true, message: "Please specify stump position", trigger: ['blur', 'change'],}],
      current_stump_high_is_less_than_12: [{
        required: true,
        message: "Please select an option",
        trigger: ['blur', 'change'],
      }],
    });

    const getApis = () =>
        ApiService.post('quote/apis', {})
            .then(response => apis.value = response.data)

    onMounted(getApis)

    const submit = () => {
      if (!formRef.value) {
        return;
      }

      formRef.value.validate((valid: boolean) => {
        if (valid) {
          loading.value = true;

          ApiService.post('quote/create', {...targetData})
              .then(() => {
                ctx.emit('reloadQuotes');
                formRef.value.resetFields();
                hideModal('new_quote_modal');
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
      apis,
      rules,
      submit,
      loading,
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

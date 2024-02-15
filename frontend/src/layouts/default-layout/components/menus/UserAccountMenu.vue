<template>
  <!--begin::Menu-->
  <div
      class="menu menu-sub menu-sub-dropdown menu-column menu-rounded menu-gray-600 menu-state-bg-light-primary fw-semibold py-4 fs-6 w-275px"
      data-kt-menu="true"
  >
    <!--begin::Menu item-->
    <div class="menu-item px-3">
      <div class="menu-content d-flex align-items-center px-3">
        <!--begin::Avatar-->
        <div class="symbol symbol-30px me-3">
          <img alt="Logo" :src="getAssetPath('media/avatars/blank.png')"/>
        </div>
        <!--end::Avatar-->

        <!--begin::Username-->
        <div class="d-flex flex-column">
          <div class="fw-bold d-flex align-items-center fs-5">
            {{ authStore.getUser()?.name }}
            <span class="badge badge-light-success fw-bold fs-9 px-2 py-1 ms-2">
              {{ authStore.getUser()?.role }}
            </span>
          </div>
          <a class="fw-semibold text-muted text-hover-primary fs-7"
          >{{ authStore.getUser()?.email }}</a
          >
        </div>
        <!--end::Username-->
      </div>
    </div>
    <!--end::Menu item-->

    <!--begin::Menu separator-->
    <div class="separator my-2"></div>
    <!--end::Menu separator-->

    <!--begin::Menu item-->
    <div class="menu-item px-5" v-if="authStore.getUser()?.id">
      <router-link :to="{name:'edit-user', params:{id:authStore.getUser()?.id}}" class="menu-link px-5">
        My Profile
      </router-link>
    </div>
    <!--end::Menu item-->

    <!--begin::Menu item-->
    <!--    <div class="menu-item px-5">-->
    <!--      <router-link to="/pages/profile/overview" class="menu-link px-5">-->
    <!--        <span class="menu-text">My Projects</span>-->
    <!--        <span class="menu-badge">-->
    <!--          <span class="badge badge-light-danger badge-circle fw-bold fs-7"-->
    <!--            >3</span-->
    <!--          >-->
    <!--        </span>-->
    <!--      </router-link>-->
    <!--    </div>-->
    <!--end::Menu item-->

    <!--begin::Menu item-->
    <!--    <div-->
    <!--      class="menu-item px-5"-->
    <!--      data-kt-menu-trigger="hover"-->
    <!--      data-kt-menu-placement="left-start"-->
    <!--      data-kt-menu-flip="center, top"-->
    <!--    >-->
    <!--      <router-link to="/pages/profile/overview" class="menu-link px-5">-->
    <!--        <span class="menu-title">My Subscription</span>-->
    <!--        <span class="menu-arrow"></span>-->
    <!--      </router-link>-->

    <!--      &lt;!&ndash;begin::Menu sub&ndash;&gt;-->
    <!--      <div class="menu-sub menu-sub-dropdown w-175px py-4">-->
    <!--        &lt;!&ndash;begin::Menu item&ndash;&gt;-->
    <!--        <div class="menu-item px-3">-->
    <!--          <router-link to="/pages/profile/overview" class="menu-link px-5">-->
    <!--            Referrals-->
    <!--          </router-link>-->
    <!--        </div>-->
    <!--        &lt;!&ndash;end::Menu item&ndash;&gt;-->

    <!--        &lt;!&ndash;begin::Menu item&ndash;&gt;-->
    <!--        <div class="menu-item px-3">-->
    <!--          <router-link to="/pages/profile/overview" class="menu-link px-5">-->
    <!--            Billing-->
    <!--          </router-link>-->
    <!--        </div>-->
    <!--        &lt;!&ndash;end::Menu item&ndash;&gt;-->

    <!--        &lt;!&ndash;begin::Menu item&ndash;&gt;-->
    <!--        <div class="menu-item px-3">-->
    <!--          <router-link to="/pages/profile/overview" class="menu-link px-5">-->
    <!--            Payments-->
    <!--          </router-link>-->
    <!--        </div>-->
    <!--        &lt;!&ndash;end::Menu item&ndash;&gt;-->

    <!--        &lt;!&ndash;begin::Menu item&ndash;&gt;-->
    <!--        <div class="menu-item px-3">-->
    <!--          <router-link-->
    <!--            to="/pages/profile/overview"-->
    <!--            class="menu-link d-flex flex-stack px-5"-->
    <!--          >-->
    <!--            Statements-->

    <!--            <i-->
    <!--              class="fas fa-exclamation-circle ms-2 fs-7"-->
    <!--              data-bs-toggle="tooltip"-->
    <!--              title="View your statements"-->
    <!--            ></i>-->
    <!--          </router-link>-->
    <!--        </div>-->
    <!--        &lt;!&ndash;end::Menu item&ndash;&gt;-->

    <!--        &lt;!&ndash;begin::Menu separator&ndash;&gt;-->
    <!--        <div class="separator my-2"></div>-->
    <!--        &lt;!&ndash;end::Menu separator&ndash;&gt;-->

    <!--        &lt;!&ndash;begin::Menu item&ndash;&gt;-->
    <!--        <div class="menu-item px-3">-->
    <!--          <div class="menu-content px-3">-->
    <!--            <label-->
    <!--              class="form-check form-switch form-check-custom form-check-solid"-->
    <!--            >-->
    <!--              <input-->
    <!--                class="form-check-input w-30px h-20px"-->
    <!--                type="checkbox"-->
    <!--                value="1"-->
    <!--                checked-->
    <!--                name="notifications"-->
    <!--              />-->
    <!--              <span class="form-check-label text-muted fs-7">-->
    <!--                Notifications-->
    <!--              </span>-->
    <!--            </label>-->
    <!--          </div>-->
    <!--        </div>-->
    <!--        &lt;!&ndash;end::Menu item&ndash;&gt;-->
    <!--      </div>-->
    <!--      &lt;!&ndash;end::Menu sub&ndash;&gt;-->
    <!--    </div>-->
    <!--end::Menu item-->

    <!--begin::Menu item-->
    <!--    <div class="menu-item px-5">-->
    <!--      <router-link to="/pages/profile/overview" class="menu-link px-5">-->
    <!--        My Statements-->
    <!--      </router-link>-->
    <!--    </div>-->
    <!--end::Menu item-->

    <!--begin::Menu separator-->
    <div class="separator my-2"></div>
    <!--end::Menu separator-->

    <!--begin::Menu item-->
    <!--    <div-->
    <!--      class="menu-item px-5"-->
    <!--      data-kt-menu-trigger="hover"-->
    <!--      data-kt-menu-placement="left-start"-->
    <!--      data-kt-menu-flip="center, top"-->
    <!--    >-->
    <!--      <router-link to="/pages/profile/overview" class="menu-link px-5">-->
    <!--        <span class="menu-title position-relative">-->
    <!--          Language-->
    <!--          <span-->
    <!--            class="fs-8 rounded bg-light px-3 py-2 position-absolute translate-middle-y top-50 end-0"-->
    <!--          >-->
    <!--            {{ currentLangugeLocale.name }}-->
    <!--            <img-->
    <!--              class="w-15px h-15px rounded-1 ms-2"-->
    <!--              :src="currentLangugeLocale.flag"-->
    <!--              alt="metronic"-->
    <!--            />-->
    <!--          </span>-->
    <!--        </span>-->
    <!--      </router-link>-->

    <!--      &lt;!&ndash;begin::Menu sub&ndash;&gt;-->
    <!--      <div class="menu-sub menu-sub-dropdown w-175px py-4">-->
    <!--        &lt;!&ndash;begin::Menu item&ndash;&gt;-->
    <!--        <div class="menu-item px-3">-->
    <!--          <a-->
    <!--            @click="setLang('en')"-->
    <!--            href="#"-->
    <!--            class="menu-link d-flex px-5"-->
    <!--            :class="{ active: currentLanguage === 'en' }"-->
    <!--          >-->
    <!--            <span class="symbol symbol-20px me-4">-->
    <!--              <img-->
    <!--                class="rounded-1"-->
    <!--                :src="getAssetPath('media/flags/united-states.svg')"-->
    <!--                alt="metronic"-->
    <!--              />-->
    <!--            </span>-->
    <!--            English-->
    <!--          </a>-->
    <!--        </div>-->
    <!--        &lt;!&ndash;end::Menu item&ndash;&gt;-->

    <!--        &lt;!&ndash;begin::Menu item&ndash;&gt;-->
    <!--        <div class="menu-item px-3">-->
    <!--          <a-->
    <!--            @click="setLang('es')"-->
    <!--            href="#"-->
    <!--            class="menu-link d-flex px-5"-->
    <!--            :class="{ active: currentLanguage === 'es' }"-->
    <!--          >-->
    <!--            <span class="symbol symbol-20px me-4">-->
    <!--              <img-->
    <!--                class="rounded-1"-->
    <!--                :src="getAssetPath('media/flags/spain.svg')"-->
    <!--                alt="metronic"-->
    <!--              />-->
    <!--            </span>-->
    <!--            Spanish-->
    <!--          </a>-->
    <!--        </div>-->
    <!--        &lt;!&ndash;end::Menu item&ndash;&gt;-->

    <!--        &lt;!&ndash;begin::Menu item&ndash;&gt;-->
    <!--        <div class="menu-item px-3">-->
    <!--          <a-->
    <!--            @click="setLang('de')"-->
    <!--            href="#"-->
    <!--            class="menu-link d-flex px-5"-->
    <!--            :class="{ active: currentLanguage === 'de' }"-->
    <!--          >-->
    <!--            <span class="symbol symbol-20px me-4">-->
    <!--              <img-->
    <!--                class="rounded-1"-->
    <!--                :src="getAssetPath('media/flags/germany.svg')"-->
    <!--                alt="metronic"-->
    <!--              />-->
    <!--            </span>-->
    <!--            German-->
    <!--          </a>-->
    <!--        </div>-->
    <!--        &lt;!&ndash;end::Menu item&ndash;&gt;-->

    <!--        &lt;!&ndash;begin::Menu item&ndash;&gt;-->
    <!--        <div class="menu-item px-3">-->
    <!--          <a-->
    <!--            @click="setLang('ja')"-->
    <!--            href="#"-->
    <!--            class="menu-link d-flex px-5"-->
    <!--            :class="{ active: currentLanguage === 'ja' }"-->
    <!--          >-->
    <!--            <span class="symbol symbol-20px me-4">-->
    <!--              <img-->
    <!--                class="rounded-1"-->
    <!--                :src="getAssetPath('media/flags/japan.svg')"-->
    <!--                alt="metronic"-->
    <!--              />-->
    <!--            </span>-->
    <!--            Japanese-->
    <!--          </a>-->
    <!--        </div>-->
    <!--        &lt;!&ndash;end::Menu item&ndash;&gt;-->

    <!--        &lt;!&ndash;begin::Menu item&ndash;&gt;-->
    <!--        <div class="menu-item px-3">-->
    <!--          <a-->
    <!--            @click="setLang('fr')"-->
    <!--            href="#"-->
    <!--            class="menu-link d-flex px-5"-->
    <!--            :class="{ active: currentLanguage === 'fr' }"-->
    <!--          >-->
    <!--            <span class="symbol symbol-20px me-4">-->
    <!--              <img-->
    <!--                class="rounded-1"-->
    <!--                :src="getAssetPath('media/flags/france.svg')"-->
    <!--                alt="metronic"-->
    <!--              />-->
    <!--            </span>-->
    <!--            French-->
    <!--          </a>-->
    <!--        </div>-->
    <!--        &lt;!&ndash;end::Menu item&ndash;&gt;-->
    <!--      </div>-->
    <!--      &lt;!&ndash;end::Menu sub&ndash;&gt;-->
    <!--    </div>-->
    <!--end::Menu item-->

    <!--begin::Menu item-->
    <!--    <div class="menu-item px-5 my-1">-->
    <!--      <router-link to="/pages/profile/overview" class="menu-link px-5">-->
    <!--        Account Settings-->
    <!--      </router-link>-->
    <!--    </div>-->
    <!--end::Menu item-->

    <!--begin::Menu item-->
    <div class="menu-item px-5">
      <a @click="authStore.logout" class="menu-link px-5"> Sign Out </a>
    </div>
    <!--end::Menu item-->
  </div>
  <!--end::Menu-->
</template>

<script lang="ts">
import {getAssetPath} from "@/core/helpers/assets";
import {defineComponent} from "vue";
import {useAuthStore} from "@/stores/auth";

export default defineComponent({
  name: "kt-user-menu",
  components: {},
  setup() {

    return {
      authStore: useAuthStore(),
      getAssetPath,
    };
  },
});
</script>

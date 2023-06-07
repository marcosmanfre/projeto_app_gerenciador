<script>
import SidebarLink from './SidebarLink'
import { collapsed, toggleSidebar, sidebarWidth } from './state'
export default {
  props: {},
  components: { SidebarLink },
  setup() {
    return { collapsed, toggleSidebar, sidebarWidth }
  }
}
</script>

<template>
  <div class="sidebar" :style="{ width: sidebarWidth }">
    <h1>
      <span v-if="collapsed">

      </span>
      <img v-else src="@/assets/logo.png" alt="Logo" width="100" >
    </h1>

    <SidebarLink to="/" icon="fas fa-home">Home</SidebarLink>  
    <SidebarLink to="/dashboard" icon="fas fa-users">Cadastro</SidebarLink>

   <!--  <SidebarLink to="/secao" icon="fas fa-columns">Seção</SidebarLink>

    <SidebarLink to="/analytics" icon="fas fa-chart-bar">..</SidebarLink>-->
    <!-- <SidebarLink to="/image" icon="fas fa-image">..</SidebarLink> -->

    <span
      class="collapse-icon"
      :class="{ 'rotate-180': collapsed }"
      @click="toggleSidebar"
    >
      <i class="fas fa-angle-double-left" />
    </span>
  </div>
</template>

<style>
:root {
  --sidebar-bg-color: #000201;
  --sidebar-item-hover: #000201;
  --sidebar-item-active: #000201;
}
</style>

<style scoped>
.sidebar {
  color: white;
  background-color: var(--sidebar-bg-color);
  float: left;
  position: fixed;
  z-index: 1;
  top: 0;
  left: 0;
  bottom: 0;
  padding: 0.6em;
  transition: 0.3s ease;
  display: flex;
  flex-direction: column;
}
.sidebar h1 {
  height: 3.5em;
}
.collapse-icon {
  position: absolute;
  bottom: 1;
  padding: 0.75em;
  color: rgba(255, 255, 255, 0.7);
  transition: 0.2s linear;
}
.rotate-180 {
  transform: rotate(180deg);
  transition: 0.2s linear;
}
</style>
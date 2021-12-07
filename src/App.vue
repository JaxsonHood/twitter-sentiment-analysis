<template>
  <router-view />
</template>

<script>
import { defineComponent } from "vue";

export default defineComponent({
  data: () => ({
    base_url: 'http://localhost:5000'
  })
});
</script>

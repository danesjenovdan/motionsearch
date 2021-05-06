<template>
  <div class="split-container">
    <div class="container-child">
      <div class="wrapper">
        <div class="debate-logo">
          <img src="../assets/motion-generator-logo.svg" alt="motion generator logo">
          <span>Easiest way to find a motion for debating</span>
        </div>
        <motion class="motion" :id="id" />
      </div>
    </div>
    <div class="container-child">
      <motion-comments/>
    </div>
  </div>
</template>

<script>
import Motion from '../components/Motion.vue'
import MotionComments from '../components/MotionComments.vue'

export default {
components: {
  Motion,
  MotionComments,
  }, props: [
    'id'
    ],
}

</script>

<style scoped lang="scss">
</style>

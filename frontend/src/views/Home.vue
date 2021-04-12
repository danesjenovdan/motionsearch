<template>
 <div class="split-container">
      <div class="split left">
          <motion/>
      </div>
      <div class="split hidden-xs">
        <motion-comments/>
      </div>
    </div>
</template>

<script>
  import Motion from '../components/Motion.vue'
  import Filters from '../components/Filters.vue'
  import MotionComments from '../components/MotionComments.vue'

  export default {
  components: {
    Motion,
    MotionComments
  }
}

</script>

<style scoped>

  .hidden-xs {
    height:90vh;
  }
  .background {
    background-image: linear-gradient(to right, #f5f2e8 0%, #faf9f6 100%), linear-gradient(to top, #000000 0%, #ffffff 100%);
  }

  .line {
    margin-top: 26px;
    border-top: 1px solid;
  }


</style>
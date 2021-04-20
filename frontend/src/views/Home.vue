<template>
 <div class="split-container">
      <div class="split left">
          <div class="debate-logo"><img src="../assets/motion-generator-logo.svg">&nbsp;&nbsp; Easiest way to find a motion for debating</div>
          <filters/>          
      </div>
      <div class="split-right">
        <motion-list/>
      </div>
    </div>
</template>

<script>
  import Motion from '../components/Motion.vue'
  import Filters from '../components/Filters.vue'
  import MotionComments from '../components/MotionComments.vue'
  import MotionList from '../components/MotionList.vue'

  export default {
  components: {
    Motion,
    MotionComments,
    Filters,
    MotionList,
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
  img {
    height: 80px;
  }
  .line {
    margin-top: 26px;
    border-top: 1px solid;
  }

  .debate-logo {
    display: flex;
    flex-direction: row;
    position: absolute;
    margin-top: 22px;
    align-items: center;
    justify-content: center;
    top: 0;
    left: 10%;
    /* Style for "Easiest wa" */
    color: #252525;
    font-family: Poppins;
    font-size: 18px;
    font-weight: 400;
    font-style: normal;
    letter-spacing: normal;
    line-height: 29px;
    text-align: left;
  }

</style>
<template>
 <div class="split-container">
   <div class="container-child">
     <div class="wrapper">
       <div class="debate-logo">
        <img src="../assets/motion-generator-logo.svg" alt="motion generator logo">
        <span>Easiest way to find a motion for debating</span>
      </div>
      <filters/>
    </div>
  </div>
  <div class="container-child">
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

<style scoped lang="scss">

.hidden-xs {
  height:90vh;
}

.debate-logo {
  display: none;
  margin: 20px;

  @media (min-width: 768px) {
    display: flex;
    flex-direction: column;
  }

  @media (min-width: 1200px) {
    margin: 0;
    flex-direction: row;
  }

  img {
    height: 80px;
    margin-bottom: 20px;

    @media (min-width: 1200px) {
      margin-bottom: 0;
    }
  }

  span {
    @media (min-width: 768px) {
      text-align: center;
    }

    @media (min-width: 1200px) {
      text-align: left;
    }
  }
}

</style>


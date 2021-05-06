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
</style>


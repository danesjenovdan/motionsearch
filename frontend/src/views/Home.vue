<template>
 <div class="split-container">
   <div class="container-child" :class="{ 'opened': filtersOpened }">
     <div class="wrapper">
       <div class="debate-logo">
         <img src="../assets/motion-generator-logo.svg" alt="motion generator logo">
         <span>Easiest way to find a motion for debating</span>
       </div>
       <filters @toggle-filters="toggleFilters"/>
     </div>
   </div>
   <div class="container-child">
     <motion-list type="getMotions" :headers="true" title="Motions" @toggle-filters="toggleFilters"/>
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
  },
  data() {
    return {
      filtersOpened: false
    }
  },
  methods: {
    toggleFilters() {
      this.filtersOpened = !this.filtersOpened
    }
  }
}

</script>

<style scoped lang="scss">

.container-child:first-child {
  position: absolute;
  top: 66px;
  opacity: 0;
  z-index: -1;

  &.opened {
    opacity: 1;
    z-index: 1;
    width: 100%;
  }

  @media (min-width: 992px) {
    position: static;
    opacity: 1;
    z-index: 1;
  }
}

</style>


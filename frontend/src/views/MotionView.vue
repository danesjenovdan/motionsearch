<template>
  <div class="split-container">
    <div class="container-child">
      <div class="wrapper">
        <div class="debate-logo">
        <router-link to="/"><img src="../assets/motion-generator-logo.svg" alt="motion generator logo"></router-link>
          <span>Easiest way to find a motion for debating</span>
        </div>
        <motion class="motion" :motion="motion" :id="id" />
      </div>
    </div>
    <div class="container-child">
      <motion-comments :motion="motion" :id="id"/>
    </div>
  </div>
</template>

<script>
import Motion from '../components/Motion.vue'
import MotionComments from '../components/MotionComments.vue'

export default {
  data() {
    return {
      motion: {},
      }
    },
  components: {
    Motion,
    MotionComments,
    },
  props: ['id'],
  async created() {
    this.motion = await this.$store.dispatch('getMotion', {id: this.id})
    this.$store.state.motions.motion = this.motion
    this.votes = await this.$store.dispatch('getUpvotes')
    const choice = this.votes.find(vote => vote.motion === this.motion.id)
    if (choice) this.motion.choice = choice.choices;
  }
}

</script>

<style scoped lang="scss">
</style>

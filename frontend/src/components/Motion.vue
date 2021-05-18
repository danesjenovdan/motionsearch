<template>
<div class="parentContainer">
  <div class="motionButtons">
    <voting :choice="motion.choice" :votes="motion.votes" :id="id"/>
    <favourite :motion="id"/>
  </div>
  <p>Added on {{motion.created_at?.split('T')[0]}}</p>
  <span class="motion-text">{{motion.topic}}</span>
  <div class="line"></div>
  <ul class="tags">
    <li class="tag" v-for="tag in motion.categories" :key="tag">
      <span class="tag-text">{{ tag }}</span>
    </li>
  </ul>
</div>
</template>

<script>
  import Favourite from './Favourite.vue'
  import Voting from './Voting.vue'
  let motion = {}
  export default {
    data() {
      return {
        motion,
      }
    },
    components: {
      Voting,
      Favourite
    },
     props: [
       'id',
       ],
    methods: {
    },
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

.parentContainer {
  display: flex;
  flex-direction: column;
  background-color: #ffffff;
  padding: 20px;
  margin-top: 100px;
  margin-bottom: 40px;

  @media (min-width: 992px) {
    padding: 40px;
  }

  p {
    font-family: "IBM Plex Mono";
    font-size: 14px;
    margin-bottom: 10px;
    margin-top: 40px;

    @media (min-width: 992px) {
      font-size: 18px;
    }
  }
}
  .motionButtons {
    display:flex;
    justify-content: space-between;
  }
  .line {
    margin-top: 26px;
    border-top: 1px solid;
  }
  .tags {
    list-style: none;
    margin-top: 20px;
    overflow: hidden;
    padding: 0;
  }
  .tag {
    display: inline-block;
    padding-left: 10px;
    padding-right: 10px;
    margin: 10px;
    border-radius: 14px;
    border: 2px solid #3098f3;
  }
  .tag-text {
    color: #000000;
    font-family: "IBM Plex Mono - Semi Bold Italic";
    font-size: 14px;
    font-weight: 400;
    font-style: normal;
    letter-spacing: normal;
    line-height: 18px;
    text-align: center;
  }

  .motion-text {
    /* Style for "EU member" */
    color: #252525;
    font-family: Poppins;
    font-size: 32px;
    line-height: 48px;

    @media (min-width: 992px) {
      font-size: 48px;
      line-height: 60px;
    }
  }

</style>

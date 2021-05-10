<template>
    <div class="parent-container">
        <div class="header"> 
          <a href="/login"><button v-show="!isAuth" class="login">LOG IN</button></a>
          <a href="/motionSuggest"><button>SUGGEST A MOTION</button></a>
        </div>
        <div class="line"/>
        <div class="motions-container">
            <div class="motions-title-bar">
              <h3>Motions </h3>
              <div class="motions-sort">
                <p>Sort by</p>
                <div class="sort-button"><span class="sort-button-text"><b>Date Added</b></span></div>
                <div class="sort-button"><span class="sort-button-text"><b>Quality</b></span></div>
              </div>
            </div>
            <div class="motions-list" v-for="motion in motions" :key="motion.id">
              <div class="motion-text-container">
                <p class="motions-date">Added on {{motion.created_at}}</p>
                <a :href="'/motion/'+motion.id"><p class="motions-title">{{motion.topic}}</p></a>
              </div>
              <div class="votes">
                <voting :votes="motion.votes" />
              </div>
          </div>
    </div>
  </div>
</template>

<script>
  import Voting from './Voting.vue'

  let motions = [];
  let page = 1;
  let refresh = true;
  export default {
    data() {
      return {
        motions,
        page,
        refresh,
        isAuth: false
      }
    },
    components: {
      Voting
    },
    methods: {
      async loadNextPage() {
        try {
          this.page += 1;
          const result = await this.$store.dispatch('getMotions', {page: this.page})
          if(result) this.motions = this.motions.concat(result)
          else this.page -= 1
          this.refresh = true
        } catch (error) {
          this.refresh = true
        }
      },
      handleScroll(e) {
        // compare height of motions-container to window height to enable next scrolling
        let element = document.querySelector('.motions-container')
        if ( element.getBoundingClientRect().bottom < window.innerHeight && this.refresh) {
          this.loadNextPage()
          this.refresh = false
        }
      }
    },
    mounted() {
      window.addEventListener("scroll", this.handleScroll)
    },
    unmounted() {
      window.removeEventListener("scroll", this.handleScroll)
    },
    async created() {
      this.isAuth = await this.$store.dispatch('isAuth')
      this.motions = await this.$store.dispatch('getMotions', {page: 1})
    }
  }

</script>

<style scoped lang="scss">

  .header {
    margin-right: 40px;
  }
  .motions-title-bar {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    border-bottom: 1px solid black;
  }
  .motions-sort {
    display: flex;
    flex-direction: row;
    align-items: center;
  }
    .share-bar {
    position: relative;
    width: 100%;
    overflow: hidden;
    display: flex;
    flex-direction: row;
    padding: 20px;
    // background-image: linear-gradient(-62deg, #f2f6fa 0%, #dbe7f1 100%);
    background-image: linear-gradient(-62deg, #cee7fd 0%, #f7fafd 100%);
    z-index: 2;
    .share-bar-split {
        width: 100%;
        display: flex;
        flex-direction: row;
        display: flex;
        flex-wrap: wrap;
        align-content: center;
        &.hidden {
        display: none !important;
        }
    }
    h1 {
        margin-top: 0;
        // width: 100%;
    }
    input {
        margin-left: 20px;
    }
    }
  h3 {
    color: #252525;
    font-family: "Poppins";
    font-size: 30px;
    font-weight: 700;
    font-style: normal;
    letter-spacing: normal;
    line-height: 60px;
    text-align: left;
    font-style: normal;
    letter-spacing: normal;
    line-height: normal;
  }
  .sort-button {
    /* Style for "Rounded Re" */
    border-radius: 20px;
    background-color: rgb(48, 152, 243, 0.2);
    padding: 10px;
    margin-left: 10px;
    cursor: pointer;
  }
  .sort-button-text {
    color: #000000;
    font-family: "IBM Plex Mono";
    opacity: 1;
    font-size: 14px;
    font-weight: 400;
    font-style: italic;
    letter-spacing: normal;
    line-height: 18px;
    text-align: center;
    text-transform: uppercase;
  }
  .motions-list {
    border-bottom: 1px solid black;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
    width: 100%;
  }
  .motions-date {
    color: #252525;
    font-family: "IBM Plex Mono";
    font-size: 14px;
    font-style: italic;
    letter-spacing: normal;
    line-height: 18px;
    text-align: left;
  }
  .motions-title {
    color: #252525;
    font-family: Poppins;
    font-size: 24px;
    font-weight: 400;
    font-style: normal;
    letter-spacing: normal;
    text-align: left;
  }
  .votes {
    width: 78px;
    height: 78px;
    flex-shrink: 0;
    margin-right: 20px;
    margin-left:20px;
    background-image: linear-gradient(to right, #f5f2e8 0%, #faf9f6 100%);
  }
	.parent-container {
		display:flex;
    margin: 0 auto;
    flex-direction: column;
    justify-content: center;
    align-items: initial;
    overflow-x: auto;
	}
  .favourite{
    background-image: '../assets/favourite.svg';
  }
  .background {
    background-image: linear-gradient(to right, #f5f2e8 0%, #faf9f6 100%), linear-gradient(to top, #000000 0%, #ffffff 100%);
  }

  .motions-container {
      display: flex;
      flex-direction: column;
      overflow: hidden;
      padding: 0px 40px 0px 40px;
  }
  .motionButtons {
    display:flex;
    justify-content: space-between;
  }

  .line {
    margin-top: 26px;
    margin-bottom: 30px;
    border-top: 1px solid #3098f3;
    margin-left: 0px;
    margin-right: 0px;
  }
  input {
    box-sizing: border-box;
  }
  .motion-text-container {
    display: flex;
    flex-direction: column;
  }
  .motion-text {
    /* Style for "EU member" */
    color: #252525;
    font-family: Poppins;
    font-size: 48px;
    font-weight: 400;
    font-style: normal;
    letter-spacing: normal;
    line-height: 60px;
    text-align: left;;
  }
    .login {
      border: 4px solid #ffcc00;
      background-color: #ffffff;
      color: #000000;
    }
  a {
    /* Style for "Lorem Ipsu" */
    color: #252525;
    font-family: Poppins;
    font-size: 18px;
    font-weight: 400;
    font-style: normal;
    letter-spacing: normal;
    line-height: 40px;
    text-align: left;
    text-decoration: underline;
    /* Text style for "Lorem Ipsu" */
    font-style: normal;
    letter-spacing: normal;
    line-height: normal;
  }
  button {
    box-shadow: none;
    border: none;
    max-width: 380px;
    padding-left: 30px;
    padding-right: 30px;
    height: 60px;
    border-radius: 30px;
    background-color: #3098f3;
    opacity: 0.7;
    color: #ffffff;
    font-family: "Poppins";
    font-style: italic;
    font-size: 30px;
    font-weight: 400;
    text-transform: uppercase;
    letter-spacing: 2.16px;
    display: block;
    margin: auto;
    margin-left: 25px;
    margin-top: 26px;
    cursor: pointer;
    float: right;
    white-space: nowrap;
  }
  button:disabled {
    opacity: 0.1;
  }
  button:hover {
    opacity: 1;
  }

</style>
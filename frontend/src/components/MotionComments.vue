<template>
    <div class="motionCommentsContainer">
      <div class="header">
        <div class="logo">
        <router-link to="/"><img src="../assets/motion-generator-logo.svg" alt="motion generator logo"></router-link>
        </div>
        <div class="header-buttons">
          <router-link to="/motionSuggest" class="button button--suggest"><span>Suggest a motion</span></router-link>
          <router-link to="/login" v-if="!isAuth" class="button button--pan"><span>Log in</span></router-link>
          <router-link to="/profile" v-if="isAuth" class="button button--pan"><span>Profile</span></router-link>
        </div>
      </div>
        <div class="share-bar">
          <div class="share-bar-split">
            <h1>Share this motion!</h1>
            <input type="url" class="share-input" :value="`https://motion-search-backend.lb.djnd.si/motion/${id}`">
          </div>
        </div>
        <div class="parentContainer">
          <div class="left">
            <h3>Comments</h3>
              <div v-show="isAuth" class="textAreaContainer">
                <textarea rows="3" cols="20" name="comment" id="comment"  placeholder="Write your comment here!" form="usrform"/>
                  <button class="textAreaButton" v-on:click="addUsedWhere(id)">Submit</button>
              </div>
              <div class="commentContainer" v-for="comment in comments" :key="comment._id">
                <i><p>{{comment.user.username}} {{comment.created_at?.split('T')[0]}}</p></i>
                <p>{{comment.text}}</p>
                <div>
              </div>
            </div>
          </div>
            <div v-if="whereUsed.length > 0 || links.length > 0" class="right">
              <div v-show="whereUsed" class="links">
                <h3>Where was it used</h3>
                  <p v-for="text in whereUsed" :key="text._id">{{text.value}}</p><br/>
                </div>
              <div v-show="links" class="links">
                <h3>Links</h3>
                <div v-for="link in links" :key="link._id" >
                  <a target="_blank" :href="link.value"> <p>{{link.text}}</p></a><br/>
                  </div>
                </div>
            </div>
    </div>
  </div>
</template>

<script>
  const comments = [
      ]

  export default {
    components: [
    ],
    props: [ 'id', 'motion'],
    data() {
      return {
        comments,
        comment: '',
        isAuth: false,
        links: false,
        whereUsed: false
      }
    },
    methods: {
      async addUsedWhere(id) {
        try {
          const response = await this.$store.dispatch('setComment', {text: comment.value, id})
        } catch (error) {}
        this.comments = await this.$store.dispatch('getComments', {id: id})
      },
    },
    async created() {
      this.isAuth = await this.$store.dispatch('isAuth')
      this.comments = await this.$store.dispatch('getComments', {id: this.id})
    },
    watch: {
      motion: async function(newVal, oldVal) {
        const {links, where_used} = newVal
        if(links?.length > 0) this.links = await this.$store.dispatch('getMotionAttributes', {type: 'links', filters: { id: [ links]}})
        if(where_used?.length > 0) this.whereUsed = await this.$store.dispatch('getMotionAttributes', {type: 'where-used', filters: { id: [ where_used]} })
      }
    }
  }

</script>

<style scoped lang="scss">

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  background-color: #FFFFFF;
  border-bottom: 1px solid #3098f3;
  // margin-bottom: 30px;

  @media (min-width: 768px) {
    justify-content: flex-end;
    position: static;
  }

  @media (min-width: 1200px) {
  }

  .logo {
    @media (min-width: 768px) {
      display: none;
    }

    img {
      height: 30px;
      margin-left: 20px;
    }
  }

  .btn {
    @media (max-width: 575px) {
      padding: 5px 5px;
      font-size: 10px;
    }
  }
  .button {
    margin-left:10px;
    @media (max-width: 575px) {
      padding: 5px 5px;
      font-size: 10px;
    }
  }
}

  .share-bar {
    position: relative;
    overflow: hidden;
    margin: 30px 20px 0 20px;
    display: flex;
    flex-direction: row;
    padding: 20px;
    // background-image: linear-gradient(-62deg, #f2f6fa 0%, #dbe7f1 100%);
    background-image: linear-gradient(-62deg, #cee7fd 0%, #f7fafd 100%);
    z-index: 2;

    @media (min-width: 1200px) {
      margin: 30px 40px 0 40px;
    }

    .share-bar-split {
      width: 100%;
      align-content: center;
      &.hidden {
        display: none !important;
      }

      @media (min-width: 1200px) {
        display: flex;
        flex-direction: row;
        flex-wrap: wrap;
      }
    }

    h1 {
      margin: 0 20px 0 0;
    }
  }
  .share-input {
    min-width:0; /* Remove the automatic minimum size set so the element can shrink*/
    width: 100%; /* Set any value of width here as reference*/
    flex: 1; /* make the item grow to fill the remaining space */
    font-size: 14px;
  }

  .commentContainer {
    border: 1px solid black;
    padding: 20px;
    font-family: "Ibm Plex Mono", sans-serif;
    color: #252525;
    font-size: 18px;
    i {
      font-size: 14px;
      font-style: italic;
    }
  }
  .textAreaContainer{
    display:inline-block;
    position:relative;
    margin-bottom: 20px;
  }

  .textAreaButton {
    position:absolute;
    bottom:0;
    right:25px;
    background:none;
    border:none;
    margin:0;
    padding:0;
    cursor: pointer;
    color: #3098f3;
    font-family: Poppins;
    font-size: 18px;
    font-weight: 700;
    text-decoration: underline;
    height: 60px;
  }

  textarea {
    display: block;
    resize: none;
    width: 100%;
    height: 100%;
    box-sizing: border-box;
  }

	.motionCommentsContainer {
		display:flex;
    margin: 0 auto;
    flex-direction: column;
    justify-content: center;
    align-items: initial;
	}
  .shareContainer {
    display: flex;
    flex-direction: row;
    background-image: linear-gradient(-62deg, #f2f6fa 0%, #dbe7f1 100%);
  }
  .parentContainer {
    display: flex;
    flex-direction: column-reverse;
    margin: 10px 20px 40px 20px;
    overflow: hidden;

    @media (min-width: 1200px) {
      margin: 10px 40px 40px 40px;
    }

    @media (min-width: 1200px) {
      flex-direction: row;
    }
  }
  .motionButtons {
    display:flex;
    justify-content: space-between;
  }
  .links {
    background-image: linear-gradient(-62deg, #f2f6fa 0%, #dbe7f1 100%);
    padding: 20px;
    margin-top: 20px;

    p {
      font-family: "Poppins";
    }

    h3 {
      margin-top: 0;
      color: #252525;
      font-family: "Poppins";
    }

    @media (min-width: 1200px) {
      margin-left: 20px;
    }
  }
  .left {
    display: flex;
    flex-direction: column;
    overflow-y: auto;

    @media (min-width: 1200px) {
      flex: 2 1 0;
    }

    h3 {
      color: #252525;
      font-family: "Poppins";
      margin-top: 40px;

      @media (min-width: 1200px) {
        font-size: 30px;
      }
    }
  }
  .right {
    width: 100%;

    @media (min-width: 1200px) {
      flex: 1 1 0;
    }
  }

.line {
  margin: 0 0 30px;
  border-top: 1px solid #3098f3;
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


</style>

<template>
  <div class="background">
      <div class="grandParentContaniner">
          <div class="parentContainer">
            <div class="motionButtons">
              <voting/>
              <favourite/>
            </div>
            <p>Added on 7/11/2021</p>
            <span class="motion-text">EU member states should 
                guarantee people under 25 a 
                temporary workplace when 
                they have been unemployed 
                for six months.</span>
            <div class="line"></div>
            <ul class="tags">
              <li class="tag" v-for="tag in tags" :key="tag">
                <span class="tag-text">{{ tag }}</span>
              </li>
            </ul>
      </div>
    </div>
  </div>
</template>

<script>
  import Favourite from './Favourite.vue'
  import Voting from './Voting.vue'
  const tags = [
        'culture', 
        'sport',
        'employment',
        'europian union',
        'culture', 
        'sport',
        'employment',
        'europian union'
      ]
  export default {
    components: {
      Voting,
      Favourite
    },
    data() {
      return {
        tags
      }
    }
  }

</script>

<style scoped>

	.grandParentContaniner{
		display:flex;
    margin: 0 auto; ;
    justify-content: center;
    align-items: center;
	}
  .background {
    background-image: linear-gradient(to right, #f5f2e8 0%, #faf9f6 100%), linear-gradient(to top, #000000 0%, #ffffff 100%);
  }
  .parentContainer {
      display: flex;
      flex-direction: column;
      background-color: #ffffff;
      padding: 40px;
      margin-top: 100px;
      margin-bottom: 40px;
      max-width: 30vw;
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
  input {
      box-sizing: border-box;
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
    margin-top: 26px;
    cursor: pointer;
    float: right;
  }
  button:disabled {
    opacity: 0.1;
  }
  button:hover {
    opacity: 1;
  }

</style>
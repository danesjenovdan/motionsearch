<template>
  <div class="container">
    <svg  :class="{ 'upvote-button': upSelected, 'upvote-button-unselected': !upSelected }" @click="toggleSelectedUp"  height='100px' width='100px'  fill="#000000" xmlns="http://www.w3.org/2000/svg" data-name="Layer 2" viewBox="0 0 32 32" x="0px" y="0px"><title>Arrows black</title><path d="M25.18,14.76,16.93,4.19a1.18,1.18,0,0,0-1.86,0L6.82,14.76a1.18,1.18,0,0,0,.93,1.9H9.18V26a1.74,1.74,0,0,0,2.23,1.67L15,25.87a2.3,2.3,0,0,1,2.09,0l3.54,1.81A1.74,1.74,0,0,0,22.82,26V16.67h1.43A1.18,1.18,0,0,0,25.18,14.76Z"></path></svg>
    <span class="upvotes-number">{{number}}</span>
    <svg :class="{ 'downvote-button': downSelected, 'downvote-button-unselected': !downSelected }" @click="toggleSelectedDown"  height='100px' width='100px'  fill="#000000" xmlns="http://www.w3.org/2000/svg" data-name="Layer 2" viewBox="0 0 32 32" x="0px" y="0px"><title>Arrows black</title><path d="M25.18,14.76,16.93,4.19a1.18,1.18,0,0,0-1.86,0L6.82,14.76a1.18,1.18,0,0,0,.93,1.9H9.18V26a1.74,1.74,0,0,0,2.23,1.67L15,25.87a2.3,2.3,0,0,1,2.09,0l3.54,1.81A1.74,1.74,0,0,0,22.82,26V16.67h1.43A1.18,1.18,0,0,0,25.18,14.76Z"></path></svg>
  </div>
</template>

<script>
export default {
  props: ['votes', 'id', 'choice'],
  data() {
    return{
      upSelected: false,
      downSelected: false,
      number: this.votes,
    }
  }, 
  methods: {
    toggleSelectedUp: async function () {
      this.upSelected = !this.upSelected;
      if(this.downSelected) { 
        this.downSelected = !this.downSelected;
        this.number += 1;  
      }
      this.number = this.upSelected ? this.number+1 : this.number-1
      await this.$store.dispatch('upvote', {choice: this.upSelected ? 1 : 3, id: this.id})
    },
    toggleSelectedDown: async function () {
      this.downSelected = !this.downSelected;
      if(this.upSelected) { 
        this.upSelected = !this.upSelected;
        this.number -= 1;
        }
      this.number = this.downSelected ? this.number-1 : this.number+1
      await this.$store.dispatch('upvote', {choice: this.downSelected ? 2 : 3, id: this.id})
    }
  },
  watch: { 
    votes: function(newVal, oldVal) { // watch it
      this.number = newVal
    },
    choice: function(newVal, oldVal) { // watch it
      if (newVal === 1) this.upSelected = true;
      if (newVal === 2) this.downSelected = true;
    }
  },
    async created() {
      if (this.choice === 1) this.upSelected = true;
      if (this.choice === 2) this.downSelected = true;
    }
}
</script>

<style scoped lang="scss">
  .upvote-button {
    fill: #3098f3;;
    cursor:pointer;
  }
  .upvote-button-unselected {
    fill: #9e9e9e;
    cursor:pointer;
  }
  .upvote-button-unselected:hover {
    fill: #3098f3;;
  }
  .downvote-button {
    fill: #f25049;
    transform: rotate(180deg);
    cursor:pointer;
  }
  .downvote-button-unselected {
    fill: #9e9e9e;
    transform: rotate(180deg);
    cursor:pointer;
  }
  .downvote-button-unselected:hover {
    fill: #f25049;
  }

  .container {
    display: flex;
    flex-direction: column;
    width: 75px;
    height: 75px;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    margin-right: 20px;
    background-image: linear-gradient(to right, #f5f2e8 0%, #faf9f6 100%);
  }
  img {
    cursor: pointer;
  }
  .upvotes-number {
    color: #252525;
    font-family: Poppins;
    font-size: 18px;
    font-weight: 700;
    font-style: normal;
    letter-spacing: normal;
    text-align: center;
  }
</style>
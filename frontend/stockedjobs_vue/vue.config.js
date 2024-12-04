const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    server: "https://scaling-trout-x5rg97x4jvqw29q.github.dev/",
    client: {
      webSocketURL: {
        protocol: 'wss', // Use Secure WebSocket
      },
    },
  }
})

const webpack = require('webpack');
const resolve = require('path').resolve;
const config = {
    devtool: 'eval-source-map',
    entry: __dirname + '/js/index.jsx',
    output:{
        path: resolve('../public'),
        filename: 'bundle.js',
        publicPath: resolve('../public')
},
resolve: {
    extensions: ['.js','.jsx','.css']
 },
 module: {
  rules: [
  {
   test: /\.jsx?/,
   loader: 'babel-loader',
   exclude: /node_modules/,
   query:{
     presets: ['react','es2015']
   },
   },
   {
         test: /\.css$/,
         loader: 'style-loader!css-loader?modules'
  }]
 }
};
module.exports = config;

module.exports = {  entry: './src/index.js',  output: {    path: __dirname + '/dist',    publicPath: '/',    filename: 'bundle.js'  },  devServer: {    contentBase: './dist',  },  module: {    rules: [    {      test: /\.(js|jsx)$/,      exclude: /node_modules/,      use: ['babel-loader']    }    ]  },};
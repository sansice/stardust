var path = require('path');
module.exports = {
    devtool: 'eval-source-map',
    entry: './book_search/web/js/index.jsx',
    mode: 'development',
    watch: true,
    output: {
        path: path.resolve(__dirname, 'book_search', 'web', 'dist'),
        publicPath: './book_search/web/js',
        filename: 'bundle.js'
    },
    resolve: {
        extensions: ['.js','.jsx','.css']
     },
    devServer: {
        contentBase: './dist',
    },
    module: {
        rules: [    {
            test: /\.(js|jsx)$/,
            exclude: /node_modules/,
            use: ['babel-loader']
        }    ]
    },
};
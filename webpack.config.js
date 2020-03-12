var path = require("path");
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');
var BundleAnalyzerPlugin = require('webpack-bundle-analyzer').BundleAnalyzerPlugin;
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const devMode = process.env.NODE_ENV !== 'production'

// refer https://github.com/owais/django-webpack-loader
// https://github.com/owais/webpack-bundle-tracker
// https://getbootstrap.com/docs/4.0/getting-started/webpack/
// https://medium.com/a-beginners-guide-for-webpack-2/webpack-loaders-css-and-sass-2cc0079b5b3a


// where to emit the bundles it creates and how to name these files
const output = {
  path: path.resolve(__dirname+'/static/bundles'),
  filename: `[name]${devMode ? '' : '-[hash]'}.js`,
  chunkFilename: `[name]${devMode ? '' : '-[hash]'}.js`,
  publicPath: '/static/bundles/',
}

module.exports = {
  context: __dirname,
  mode: devMode ? 'development' : 'production',
  // indicates which module webpack should use to begin out its internal dependency graph
  entry: {
    main_css: './static/js/css',
    libs: './static/js/main',
    team_member_edit: './team_member/static/js/team_member_edit',
    task_add: './task/static/js/task_add'
  },
  optimization: {
    runtimeChunk: "single",
    splitChunks: {
      cacheGroups: {
        lazy_libraries: {
          test: /[\\/]node_modules[\\/]/,
          chunks: 'async',
        },
        vendor: {
          test: /[\\/]node_modules[\\/]/,
          name: 'vendor',
          chunks: 'all',
        }
      }
    }
  },
  output,
  // perform a wider range of tasks like bundle optimization ...
  plugins: [
    // new BundleAnalyzerPlugin({
    //   analyzerMode: 'static'
    // }),
    new BundleTracker({
      filename: './webpack-stats.json'
    }),
    new webpack.ProvidePlugin({
      $: 'jquery',
      jQuery: 'jquery',
      'window.jQuery': 'jquery',
      Popper: ['popper.js', 'default'],
    }),
    new MiniCssExtractPlugin({
      filename: devMode ? '[name].css' : '[name].[hash].css',
      chunkFilename: devMode ? '[id].css' : '[id].[hash].css',
    })
  ],
  module: {
    // loaders are transformation that are applied to the source code of a module

    // Webpack by itself only knows javascript, so when we want it to pack any
    // other type of resources like .css or .scss or .ts, webpack needs help
    // in order to compile and bundle those non-javascript types of resources.
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: ['babel-loader']
      },
      {
        test: /\.vue$/,
        loader: 'vue-loader'
      },
      {
        test: /\.(sa|sc|c)ss$/,
        use: [{
          loader: MiniCssExtractPlugin.loader, // inject CSS to page
        }, {
          loader: 'css-loader', // translates CSS into CommonJS modules
        }, {
          loader: 'postcss-loader', // Run post css actions
          options: {
            plugins: function () { // post css plugins, can be exported to postcss.config.js
              return [
                require('precss'),
                require('autoprefixer')
              ];
            }
          }
        }, {
          loader: 'sass-loader' // compiles SASS to CSS
        }]
      },
      {
        test: /\.(ttf|eot|woff|woff2|svg)$/,
        use: {
          loader: "file-loader",
          options: {
            name: "fonts/[name].[ext]"
          }
        },
      },
    ]
  },
  resolve: {
    // Automatically resolve certain extensions. enables users to leave off
    // the extension when importing:
    extensions: ['*', '.js', '.scss', '.vue'],
    // Create aliases to import or require certain modules more easily.
    alias: {
      static: path.resolve(__dirname, 'static')
    }
  }

};

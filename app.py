from flask import Flask,render_template,jsonify
import crawling

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('main.html')


@app.route('/nations/stocks/<stock_name>', methods=['GET'])
def get_stock(stock_name):
    # print(crawling.crawl(stock_name))
    # return jsonify({"return":crawling.crawl(stock_name)})
    return crawling.crawl(stock_name)


@app.route('/nations/indices', methods=['GET'])
def get_indices():
    # return craling.crawl()
    return crawling.crawl_indices()

@app.route('/nations/future_indices', methods=['GET'])
def get_future_indices():
    return "선물 테스트"

if __name__ == '__main__':
    app.run('0.0.0.0',port=5000,debug=True)
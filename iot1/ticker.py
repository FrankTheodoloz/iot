import plotly.graph_objs as go
import yfinance as yf


def get_chart(ticker):
    data = yf.download(tickers=ticker, period='24h', interval='15m', rounding=True)
    fig = go.Figure()
    fig.add_trace(go.Candlestick())

    fig.add_trace(
        go.Candlestick(x=data.index, open=data['Open'], high=data['High'], low=data['Low'], close=data['Close'],
                       name='market data'))

    fig.update_layout(title=f'{ticker} price', yaxis_title='USD')

    fig.update_xaxes(rangeslider_visible=True, rangeselector=dict(buttons=list(
        [dict(count=15, label='15m', step="minute", stepmode="backward"),
         dict(count=45, label='45m', step="minute", stepmode="backward"),
         dict(count=1, label='1h', step="hour", stepmode="backward"),
         dict(count=6, label='6h', step="hour", stepmode="backward"), dict(step="all")])))

    # fig.show()
    fig.write_html("/var/www/html/ticker/content.html")

# get_chart('BTC-USD')

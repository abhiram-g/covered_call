import matplotlib.pyplot as plt
import numpy as np

def update_annot(ind):
    x,y = line.get_data()
    annot.xy = (x[ind["ind"][0]], y[ind["ind"][0]])
    # text = "{}, {}".format(" ".join(list(map(str,ind["ind"]))), 
    #                        " ".join([names[n] for n in ind["ind"]]))
    text = 'Closing price: ' + str(x[ind['ind'][0]]) + ', P&L: ' + str(y[ind['ind'][0]])
    annot.set_text(text)
    annot.get_bbox_patch().set_alpha(0.4)


def hover(event):
    vis = annot.get_visible()
    if event.inaxes == ax:
        cont, ind = line.contains(event)
        if cont:
            update_annot(ind)
            annot.set_visible(True)
            fig.canvas.draw_idle()
        else:
            if vis:
                annot.set_visible(False)
                fig.canvas.draw_idle()


def plot(x_arr, y_arr, strike_price, cmp):
    global annot, ax, line, fig, x, y
    x = x_arr
    y = y_arr

    fig,ax = plt.subplots()
    line, = plt.plot(x,y)
    ax.set_title('Covered call P&L')
    ax.set_xlabel('Closing price')
    ax.set_ylabel('P & L')
    # line.set_label('')
    ax.plot([strike_price[0]], [strike_price[1]], 'sr', label='Strike price')
    ax.plot([cmp[0]], [cmp[1]], '^g', label='CMP when purchased')
    ax.legend()
    annot = ax.annotate("", xy=(0,0), xytext=(-20,20),textcoords="offset points",
                        bbox=dict(boxstyle="round", fc="w"),
                        arrowprops=dict(arrowstyle="->"))
    annot.set_visible(False)
    fig.canvas.mpl_connect("motion_notify_event", hover)

    plt.show()


if __name__ == '__main__':
    x = np.sort(np.random.rand(15))
    y = np.sort(np.random.rand(15))

    plot(x,y)

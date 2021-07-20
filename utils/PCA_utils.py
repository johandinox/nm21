from sklearn.decomposition import PCA 
import scipy
import seaborn as sns;

def conactinate_nth_items(startlist):
    concatinated_column_vectors = []
    for c in range(len(max(startlist, key=len))):
        column = []
        for t in range(len(startlist)):
            if c <= len(startlist[t])-1:
                column = column + [startlist[t][c]]
        concatinated_column_vectors.append(column)
    return concatinated_column_vectors

#### plot average activity (across trials) heatmap for each region

def plot_zscored_activity_heatmap(rfilt_activity,input_regions,region):
    mean_activity_all = []
    for unit in range(len(rfilt_activity[region])):
        start = -250
        end = 0
        trial_activity = []
        for i in range(int(len(activity[unit])/250)):
            start = start + 250
            end = end + 250
            trial_activity = trial_activity + [list(rfilt_activity[region][unit][start:end])]

    ## calculate mean acitvity across trials 
        mean_activity = []
        for item in conactinate_nth_items(trial_activity):
            mean_activity = mean_activity + [np.mean(item)]
        mean_activity_all = mean_activity_all + [mean_activity]

    # plot heatmap of activity across session(?)
    smoothed_z_scored_activity= []
    peak_activity= []
    for i,neuron in enumerate(mean_activity_all):
        val = moving_average(scipy.stats.zscore(neuron),5)
        if np.isnan(val[0]):
            val = np.zeros(len(val))
        smoothed_z_scored_activity = smoothed_z_scored_activity + [val]
        peak_activity = peak_activity + [np.where(smoothed_z_scored_activity[i] == max(smoothed_z_scored_activity[i]))[0][0]]

    rearranged_zs_activity = np.array(smoothed_z_scored_activity)[np.argsort(peak_activity)]

    print(input_regions[region])

    ax = sns.heatmap(np.array(rearranged_zs_activity), xticklabels=25, yticklabels=False,cmap="viridis")
    plt.axvline(x=50, color = 'red')

def plot_pca_varexp_outcome(pca):

    var_explained = np.cumsum(pca.explained_variance_ratio_)/sum(pca.explained_variance_ratio_)

    fig, ax = plt.subplots(1, 1,figsize=(20, 10))
    ax.plot(var_explained,'o-')
    ax.set_ylabel('Varience  explained')
    ax.set_xlabel('components')

    zoom_in = np.where(var_explained > 0.8)[0][0]
    # Create a Rectangle patch
    rect = patches.Rectangle((0, 0), zoom_in, 0.8, linewidth=1, edgecolor='r', facecolor='none')

    # Add the patch to the Axes
    ax.add_patch(rect)

    fig, ax = plt.subplots(1, 1,figsize=(20, 10))
    ax.plot(np.cumsum(pca.explained_variance_ratio_)/sum(pca.explained_variance_ratio_),'o-')
    ax.set_ylabel('Varience  explained')
    ax.set_xlabel('components')
    ax.set_xlim([0,zoom_in])

    print('80% var explained by ' + str(zoom_in) + ' components')

def PCA_all_trials(rfilt_activity,components = 5):
    mean_sbtrct = rfilt_activity - np.mean(rfilt_activity, axis=1)[:, np.newaxis]
    model = PCA(n_components = components).fit(mean_sbtrct.T)
    W = model.components_
    plot_pca_varexp_outcome(model)

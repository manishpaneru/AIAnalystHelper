import matplotlib.pyplot as plt
import seaborn as sns

def create_visualization(df, viz_config):
    """
    Create visualizations based on the API suggestions
    
    Args:
        df (pandas.DataFrame): The dataset
        viz_config (dict): Visualization configuration from API
    """
    # Set the figure size
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # Set the style using seaborn's default
    sns.set_theme(style="whitegrid")
    
    viz_type = viz_config.get('type', 'bar')
    params = viz_config.get('params', {})
    
    if viz_type == 'bar':
        # Create bar plot with specific columns
        sns.barplot(
            data=df,
            x=params.get('x'),
            y=params.get('y'),
            ax=ax
        )
        
    elif viz_type == 'line':
        # Create line plot with specific columns
        sns.lineplot(
            data=df,
            x=params.get('x'),
            y=params.get('y'),
            ax=ax
        )
    
    # Set title and labels
    ax.set_title(params.get('title', ''), pad=20)
    ax.set_xlabel(params.get('xlabel', ''))
    ax.set_ylabel(params.get('ylabel', ''))
    
    # Rotate x-axis labels if they're too long
    plt.xticks(rotation=45, ha='right')
    
    plt.tight_layout()
    return fig 
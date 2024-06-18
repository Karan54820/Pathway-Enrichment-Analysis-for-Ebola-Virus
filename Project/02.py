import streamlit as st
import pandas as pd
from gprofiler import GProfiler
from PIL import Image
import matplotlib.pyplot as plt


def process_data(df):

    gg = df["GeneID"].tolist()



    gene_list = gg[:216]


    gp = GProfiler(return_dataframe=True)
    pathway_enrichment = gp.profile(organism='hsapiens', query=gene_list, sources=['KEGG'])

    print(pathway_enrichment)

    sorted_results = pathway_enrichment.sort_values(by='precision', ascending=False)

    return sorted_results

st.title("Pathway Enrichment Analyzer For Ebola Virus")

image = Image.open('logo1.jpg')

st.image(image, use_column_width=True)


uploaded_file = st.file_uploader("Upload the CSV file Containing all the Differentially Expressed Genes", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Input File:")
    st.write(df)

    sorted_results = process_data(df)
    st.write("Enriched Pathways:")
    st.write(sorted_results)

    # Plotting the graph with explicit figure handling
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.barh(sorted_results['name'], sorted_results['precision'], color='skyblue')
    ax.set_xlabel('Precision')
    ax.set_ylabel('Pathway')
    ax.set_title('Pathway Enrichment Analysis')
    ax.invert_yaxis()  
    st.pyplot(fig)  

    st.markdown("""
# Output Predictions
The pathway analysis results reveal several enriched pathways associated with Ebola virus infection:

- **Ribosome:** This pathway shows a remarkable level of enrichment, with a Fold Enrichment of 21.7, suggesting a significant involvement in the Ebola virus replication process. Ribosomes are cellular structures responsible for protein synthesis. The enrichment of this pathway could indicate that Ebola virus infection may hijack the host cell's protein synthesis machinery to facilitate its own replication and protein production.

- **Coronavirus disease-COVID-19:** Interestingly, this pathway also exhibits significant enrichment. While Ebola virus and coronaviruses are distinct viruses, the enrichment of the COVID-19 pathway may suggest potential similarities or shared mechanisms between these viruses in terms of host response or pathogenesis. This could indicate common pathways activated by viral infections.

- **Malaria and African trypanosomiasis:** Although not directly related to Ebola virus, these pathways show enrichment. The enrichment of these pathways may suggest shared host response pathways or co-infections in the studied population. It implies that individuals infected with Ebola virus may also be predisposed to or co-infected with malaria or African trypanosomiasis, leading to the activation of pathways associated with both diseases.

- **Thyroid cancer:** Enrichment of this pathway is observed, indicating dysregulation of cell signaling pathways involved in cancer development. This may reflect host responses to Ebola virus infection, indicating potential alterations in cellular signaling pathways that contribute to disease pathogenesis or immune responses.
""")
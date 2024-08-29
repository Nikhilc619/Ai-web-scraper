import streamlit as st
from scrape import (
    scrape_website,
    extract_body_content,
    clean_body_content,
    split_dom_content,
)
from parse import parse_with_ollama
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Streamlit UI
st.title("AI Web Scraper")
url = st.text_input("Enter Website URL")

# Step 1: Scrape the Website
if st.button("Scrape Website"):
    if url:
        st.write("Scraping the website...")
        try:
            # Scrape the website
            dom_content = scrape_website(url)
            body_content = extract_body_content(dom_content)
            cleaned_content = clean_body_content(body_content)

            # Store the DOM content in Streamlit session state
            st.session_state.dom_content = cleaned_content

            # Display the DOM content in an expandable text box
            with st.expander("View DOM Content"):
                st.text_area("DOM Content", cleaned_content, height=300)
            
            st.success("Website scraped successfully!")
        except ValueError as ve:
            st.error(f"Error: {str(ve)}")
        except Exception as e:
            st.error(f"An error occurred while scraping the website: {str(e)}")
    else:
        st.warning("Please enter a URL before scraping.")

# Step 2: Ask Questions About the DOM Content
if "dom_content" in st.session_state:
    parse_description = st.text_area("Describe what you want to parse")

    if st.button("Scrape Website"):
     if url:
        st.write("Scraping the website...")
        try:
            # Scrape the website
            dom_content = scrape_website(url)
            if dom_content is None:
                st.error("Failed to scrape the website. Please check the URL and try again.")
            else:
                body_content = extract_body_content(dom_content)
                cleaned_content = clean_body_content(body_content)

                # Store the DOM content in Streamlit session state
                st.session_state.dom_content = cleaned_content

                # Display the DOM content in an expandable text box
                with st.expander("View DOM Content"):
                    st.text_area("DOM Content", cleaned_content, height=300)
                
                st.success("Website scraped successfully!")
        except ValueError as ve:
            st.error(f"Error: {str(ve)}")
        except Exception as e:
            st.error(f"An unexpected error occurred: {str(e)}")
    else:
        st.warning("Please enter a URL before scraping.")
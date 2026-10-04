\# REACLYST System Architecture



\## 1. Overview



REACLYST is an AI research platform for financial event and market impact analysis.



The system processes financial news, identifies relevant financial events, connects those events with companies and market data, and analyzes historical market reactions to similar events.



The architecture is designed to support both:



\- A production-style web application

\- Reproducible AI/ML research experiments



\## 2. High-Level Architecture



REACLYST will use a layered architecture:



Financial News

&#x20;      ↓

Data Ingestion

&#x20;      ↓

News Processing

&#x20;      ↓

Entity \& Event Extraction

&#x20;      ↓

Market Data Integration

&#x20;      ↓

Market Impact Analysis

&#x20;      ↓

Historical Analogue Engine

&#x20;      ↓

AI/ML Analysis

&#x20;      ↓

REST API

&#x20;      ↓

Web Application



\## 3. Main Components



\### 3.1 Data Ingestion



Responsible for collecting and preparing:



\- Financial news articles

\- Company information

\- Historical market data

\- Relevant financial metadata



\### 3.2 News Intelligence



Responsible for understanding financial news.



Initial responsibilities include:



\- Text cleaning

\- Entity extraction

\- Company identification

\- Financial event classification

\- Sentiment analysis

\- Confidence estimation



\### 3.3 Event Engine



The Event Engine converts financial news into structured financial events.



Example:



News:

A company announces a major acquisition.



Structured event:



\- Company: Example Corp

\- Event Type: Acquisition

\- Event Direction: Positive/Negative/Neutral

\- Event Date: YYYY-MM-DD

\- Confidence: Model-generated score



\### 3.4 Market Impact Engine



The Market Impact Engine studies what happened in the market around an event.



Possible measurements include:



\- Returns

\- Abnormal returns

\- Cumulative abnormal returns

\- Trading volume

\- Volatility

\- Event-window performance



\### 3.5 Historical Analogue Engine



This component searches historical events for events that are similar to a newly detected event.



Similarity may consider:



\- Event type

\- Company

\- Industry

\- News representation

\- Market conditions

\- Event context



The system can then show how similar historical events affected the market.



\### 3.6 Market Regime Engine



The system will eventually classify the broader market environment.



Possible regimes include:



\- Bull market

\- Bear market

\- High volatility

\- Low volatility

\- Strong trend

\- Weak trend



Historical event reactions can then be compared across different market regimes.



\### 3.7 AI/ML Research Layer



This layer will contain experiments and models used to investigate the project's research questions.



Potential approaches include:



\- Sentiment analysis

\- Traditional NLP

\- Transformer-based representations

\- Embedding-based similarity

\- Machine learning classifiers

\- Event-aware models



\## 4. Backend



The backend will initially use Python and FastAPI.



Responsibilities:



\- API endpoints

\- Data processing

\- Model inference

\- Market analysis

\- Database communication

\- Authentication if required later



\## 5. Frontend



The frontend will provide an interactive research interface.



Planned technologies:



\- React

\- TypeScript

\- Tailwind CSS

\- Interactive visualization library



The interface should emphasize:



\- Financial information density

\- Clear data visualization

\- Interactive exploration

\- Research transparency

\- Modern visual design



\## 6. Database



PostgreSQL will be used for structured application data.



Potential entities include:



\- Companies

\- News articles

\- Events

\- Market observations

\- Event reactions

\- Experiments

\- Model results



Vector search may be added later for historical analogue retrieval.



\## 7. Research and Experimentation



Research experiments will remain separated from production application code.



The `experiments/` directory will contain:



\- Experimental notebooks

\- Model comparisons

\- Evaluation scripts

\- Research results



This separation will help maintain reproducibility and clean software architecture.



\## 8. Testing



Testing will be included throughout development.



Planned testing areas:



\- Unit tests

\- Integration tests

\- API tests

\- Data validation

\- Model evaluation

\- End-to-end testing



\## 9. Deployment



The project is expected to use:



\- GitHub

\- GitHub Actions

\- Docker

\- Cloud deployment



Deployment architecture will be finalized after the core application has been developed.



\## 10. Design Principles



REACLYST will follow these principles:



1\. Separation of concerns

2\. Reproducibility

3\. Testability

4\. Modularity

5\. Clear version control

6\. Data and model lineage

7\. Avoidance of data leakage

8\. Reproducible experiments

9\. Explainable results where possible

10\. Separation of research code from production code


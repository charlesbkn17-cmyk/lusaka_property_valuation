# GIS and Machine Learning-Based Automated Valuation Model for Property Tax Assessment in Lusaka

## Professional Presentation Slides

---

## SLIDE 1: Title Slide

**Development of a GIS and Machine Learning-Based Automated Valuation Model for Property Tax Assessment in Lusaka**

Charles Silunjili (2022079761)
Cosmas Mwanza (2022091485)
Isaac Lungu (2022096193)

Supervisor: Mr. Chibesa Mubanga

Department of Library and Information Science
The University of Zambia

2026

---

## SLIDE 2: Problem Statement

### The Challenge

- Property valuation in Lusaka relies on **manual, outdated processes**
- Rapid urban growth outpaces record updates
- **Valuation roll is incomplete** – missing properties not assessed for tax
- **7 properties absent** in Kalingalinga pilot area (12 recorded vs 19 mapped)
- Revenue loss and unfair tax distribution

### Why This Matters

- Municipal revenue generation is affected
- Tax equity is compromised
- Local authority cannot keep up with urban development

---

## SLIDE 3: Research Objectives

### Main Objective
Develop a GIS and Machine Learning-Based Automated Valuation Model for Property Tax Assessment in Lusaka

### Specific Objectives

1. Identify valuation metrics and criteria used by LCC
2. Investigate challenges in current valuation methods
3. Determine the valuation gap in pilot zone
4. Develop a Gradient Boosting AVM using geospatial data
5. Evaluate model accuracy against manual valuations

---

## SLIDE 4: Research Questions

1. **What valuation metrics are currently used?**
   - Land area, building area, location, amenity proximity

2. **What challenges exist?**
   - Incomplete records, manual processes, poor data integration

3. **What is the valuation gap?**
   - Measure missing properties and lost revenue

4. **How can we build an AVM?**
   - Using building footprints, OpenStreetMap, and valuation data

5. **How accurate can the model be?**
   - Compare predictions with existing valuations

---

## SLIDE 5: Literature Review - Key Findings

### Property Valuation Drivers
- **Structural factors**: land area, building size, construction quality
- **Locational factors**: proximity to amenities, transport, services
- **Context**: market conditions, neighborhood characteristics

### Current System Limitations
- Manual processes are time-consuming
- Valuation roll incompleteness affects revenue
- Spatial and administrative data are not integrated

### Machine Learning Solutions
- Gradient Boosting handles non-linear relationships
- Random Forest and GBM show strong performance
- GIS integration improves location representation

---

## SLIDE 6: Methodology - Research Approach

### Mixed-Methods Design

**Qualitative Component**
- Understanding valuation criteria
- Investigating operational challenges
- Contextualizing the problem

**Quantitative Component**
- Spatial analysis
- Valuation-gap detection
- Model development and evaluation

### This combination addresses both institutional and technical dimensions

---

## SLIDE 7: Methodology - Five Stages

| Stage | Activity | Purpose |
|-------|----------|---------|
| 1 | Identify valuation metrics | Ground model in real drivers |
| 2 | Investigate challenges | Understand barriers |
| 3 | Determine valuation gap | Measure undercount |
| 4 | Develop AVM | Build prediction system |
| 5 | Evaluate model | Test performance |

---

## SLIDE 8: System Architecture

### Components

1. **Data Acquisition**
   - Valuation records
   - Building footprints
   - OpenStreetMap amenity data

2. **Processing Pipeline**
   - Data cleaning and validation
   - Geospatial alignment
   - Feature engineering

3. **Machine Learning**
   - Gradient Boosting Regressor
   - Value prediction

4. **Output**
   - Dashboard
   - Gap summary
   - Valuations

---

## SLIDE 9: The Valuation Gap - Key Finding

### Kalingalinga Pilot Area

| Metric | Count |
|--------|-------|
| Recorded properties (valuation roll) | 12 |
| Mapped properties (building footprints) | 19 |
| **Valuation Gap** | **7 properties** |
| **Gap Percentage** | **58.3%** |

### Implication

Properties exist physically but are **absent from the tax database**
- Lost revenue
- Unfair tax distribution
- Incomplete property base

---

## SLIDE 10: Variables Used in Model

### Geospatial Features

**Structural Variables**
- Land area (from footprints)
- Building area
- Building count
- Building density ratio

**Locational Variables**
- Distance to schools
- Distance to markets
- Distance to hospitals
- Distance to transport routes

**Result**: Combined model reflects real property value drivers

---

## SLIDE 11: Model Development Process

```
Raw Data
    ↓
Data Cleaning & Validation
    ↓
Geospatial Overlay & Matching
    ↓
Feature Engineering
    ↓
Gradient Boosting Training
    ↓
Model Evaluation
    ↓
Dashboard & Results
```

### Key Technology: Gradient Boosting Machine

- Handles non-linear relationships
- Learns from multiple interacting features
- Suitable for complex valuation problems

---

## SLIDE 12: Model Evaluation Metrics

### Performance Measures

| Metric | Interpretation |
|--------|-----------------|
| **RMSE** | Average prediction error magnitude |
| **MAE** | Mean absolute deviation |
| **MAPE** | Percentage error rate |
| **R²** | Proportion of variance explained |

### Results

- Model achieved acceptable accuracy for pilot study
- Demonstrated learning of property value patterns
- Grounded in selected spatial and structural variables
- Viable for municipal decision-making

---

## SLIDE 13: System Dashboard

### What Users See

✓ **Valuation Gap Summary**
  - Total properties in roll
  - Total mapped properties
  - Missing properties count

✓ **Property Valuations**
  - Predicted values for all mapped properties
  - Property-by-property breakdown
  - Revenue implications

✓ **Administrative Insights**
  - Areas of concern
  - High-priority zones
  - Implementation roadmap

---

## SLIDE 14: Results Summary

### Finding 1: Incomplete Valuation Roll
- Kalingalinga had 7 missing properties
- Represents 58.3% gap in recorded properties

### Finding 2: Multi-Factor Valuation
- Property value is driven by structural AND locational factors
- GIS-based model captures both dimensions

### Finding 3: Model Viability
- Gradient Boosting achieved predictive accuracy
- System is operationally useful for municipalities

### Finding 4: Practical Impact
- System can identify missing properties
- System can estimate values for those properties

---

## SLIDE 15: Challenges & Risks

### Data Quality Risks
- Incomplete or duplicate records
- Misaligned spatial datasets
- Missing amenity information

### Model Limitations
- Limited dataset size in pilot
- Generalization to wider city needs validation
- Field verification required for missing properties

### Implementation Risks
- Institutional adoption challenges
- Data governance requirements
- Need for ongoing maintenance

---

## SLIDE 16: Resources & Feasibility

### What Was Needed

✓ Geospatial data (building footprints, OSM)
✓ Software tools (Python, GIS libraries)
✓ Computing resources
✓ Technical expertise (GIS, machine learning)

### Why It Was Feasible

✓ Open-source tools available
✓ Manageable pilot scale
✓ Clear workflow from problem to solution
✓ University support and supervision

### Scaling Considerations

→ Larger dataset needed
→ Institutional coordination required
→ Data governance framework
→ Operational support structure

---

## SLIDE 17: Contributions to Knowledge

### Academic Contributions

1. **Methodology**: Combines GIS with ML for municipal valuation
2. **Evidence**: Demonstrates valuation gap detection is possible
3. **Model**: Provides practical AVM for local government
4. **Process**: Outlines workflow for urban property systems

### Practical Contributions

1. **Tool**: Prototype system ready for expansion
2. **Approach**: Replicable across municipalities
3. **Revenue**: Framework to improve tax base
4. **Governance**: Data-driven decision support

---

## SLIDE 18: Recommendations

### For Lusaka City Council

1. **Integrate GIS** into valuation processes
2. **Adopt periodic audits** using spatial comparison
3. **Use predictive models** to supplement expert judgment
4. **Update spatial data** regularly to track change

### For Future Development

1. **Expand to wider city** beyond Kalingalinga
2. **Validate missing properties** in the field
3. **Test alternative algorithms** (Random Forest, SVR)
4. **Integrate with existing municipal systems**

---

## SLIDE 19: Future Research Directions

### Short Term
- Extend pilot study to other neighborhoods
- Field-validate detected missing properties
- Integrate with LCC operational systems

### Medium Term
- Compare multiple machine learning algorithms
- Develop real-time monitoring system
- Create training program for municipal staff

### Long Term
- City-wide implementation
- Integration with property records database
- Automated value updates with market changes
- Support for other municipalities in Zambia

---

## SLIDE 20: Key Takeaways

### The Problem
❌ Incomplete valuation rolls → lost revenue

### The Solution
✓ GIS + Machine Learning = Automated Valuation Model

### The Evidence
✓ 7 missing properties in Kalingalinga (58.3% gap)
✓ Model achieves predictive accuracy
✓ System integrates property ID and valuation

### The Impact
→ Better property tax administration
→ Fairer tax distribution
→ Improved municipal revenue
→ Foundation for smart cities in Lusaka

---

## SLIDE 21: Questions & Discussion

### Key Themes for Discussion

1. **Property identification**: How can we validate missing properties?
2. **Model accuracy**: What level of accuracy is acceptable for tax?
3. **Implementation**: What support is needed for municipal adoption?
4. **Scaling**: How do we expand from Kalingalinga to city-wide?
5. **Integration**: How does this link to broader land administration?

### Contact Information

Charles Silunjili
Cosmas Mwanza
Isaac Lungu

Department of Library and Information Science
The University of Zambia

---

## SLIDE 22: Thank You

**Development of a GIS and Machine Learning-Based Automated Valuation Model for Property Tax Assessment in Lusaka**

Thank you for your attention and engagement.

We welcome your feedback, questions, and suggestions for improvement.

---

## Presentation Notes

### Slide Design Recommendations

**Color Scheme (Professional)**
- Primary: Navy Blue (#1F3A70)
- Secondary: Teal (#008080)
- Accent: Gold (#D4AF37)
- Background: Light Gray (#F5F5F5)
- Text: Dark Gray/Black (#333333)

**Font Recommendations**
- Titles: Calibri or Arial Bold, 44-54pt
- Body: Calibri or Arial, 24-32pt
- Code/Data: Courier New, 18-24pt

**Layout Tips**
- Use consistent spacing (avoid clutter)
- Maximum 5-6 lines per slide
- Use visuals and diagrams where possible
- Keep text minimal, elaborate verbally
- Include slide numbers for reference

**Timing Guide**
- Total presentation: 15-20 minutes
- Approximately 1 minute per slide
- Leave time for questions
- Emphasize slides 9, 14, and 20 (key findings)

---

## How to Create This in PowerPoint/Google Slides

1. **Title Slide**: 
   - Background image: Urban landscape or property/buildings
   - Use gradient overlay (navy to teal)
   - White text, gold accents for titles

2. **Content Slides**:
   - Subtle gradient background (light gray to off-white)
   - Thin teal line at bottom
   - Navy headers
   - Icons where appropriate (GIS map, buildings, graph)

3. **Data Slides** (9, 12, 14):
   - Use charts/tables with navy/teal colors
   - Add visual icons to represent concepts
   - Make numbers prominent

4. **Final Slide**:
   - University logo
   - Contact information
   - Gradient background matching title slide

---

## Animation & Transitions

### Recommended Animations
- Titles: Fade in (0.5 seconds)
- Bullets: Appear one at a time (0.3 seconds)
- Images: Zoom in (0.5 seconds)
- Charts: Appear with data (1 second)

### Transitions
- Subtle fade or push (0.5-1 second)
- Avoid excessive effects
- Use consistently throughout

---

This markdown file provides the complete structure for professional presentation slides. You can use this to create slides in PowerPoint, Google Slides, or any presentation software.

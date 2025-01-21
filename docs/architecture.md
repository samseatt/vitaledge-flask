# VitalEdge Flask: Architecture Specification Document

## **1. Overview**

**VitalEdge Flask** is the internal UI designed to facilitate operations and workflows centered around **Beaker**, the bioinformatics-focused MongoDB database, and its associated pipelines. Flask provides visibility into genomic studies and variants, orchestrates bioinformatics workflows, and ensures data integrity as it progresses through the ETL pipeline into **Datalake**. Flask serves as a vital interface for researchers and bioinformaticians, enabling them to validate, monitor, and debug workflows.

## **2. Vision**

To create a streamlined and efficient interface for managing **Beaker** data and its transformation through bioinformatics pipelines, ensuring clean and reliable genomic data flows into **Datalake**.

## **3. Key Objectives**

1. **Direct Beaker Management**:
   - Provide robust interfaces to query, view, and edit Beaker’s raw genomic data (subjects, studies, variants).
   
2. **Pipeline Integration**:
   - Enable the initiation and monitoring of bioinformatics pipelines (e.g., RxGen) that process genomic data in Beaker.
   - Allow seamless tracking of pipeline progress and outcomes.

3. **Data Validation**:
   - Equip users with tools to validate pipeline outputs and identify issues before committing data to **Datalake**.

4. **Audit Trail & Provenance**:
   - Maintain a clear audit trail for data transformations from Beaker to Datalake, ensuring traceability and reproducibility.

5. **Loading Operations to Datalake**:
   - Provide visibility and control for loading Beaker data into Datalake through the formal **BRIDGE** process.
   - Ensure proper logging and monitoring of this final step.

## **4. Architecture Overview**

### **4.1 Application Layers**

1. **Frontend Layer**:
   - Built using Flask templates (Jinja2) for server-side rendering.
   - Bootstrap-based responsive design for user-friendly interfaces.

2. **Backend Layer**:
   - Flask as the primary web framework.
   - RESTful APIs for Beaker operations and pipeline orchestration.

3. **Database Layer**:
   - MongoDB (“Beaker”) as the primary data store for genomic studies and raw variant data.
   - Interface with Beaker via PyMongo for seamless querying and updates.

4. **Pipeline Orchestration**:
   - Integrate with bioinformatics pipelines (e.g., RxGen) via REST APIs or task queues.
   - Expose pipeline status, logs, and outputs to users.

5. **Data Loading (BRIDGE)**:
   - Control mechanisms for moving validated Beaker data into **Datalake**.
   - Logging and error tracking for ETL tasks.

### **4.2 Component Diagram**

```
[User] ⇒ [Flask UI] ⇒ [Beaker (MongoDB)]
                 ⇒ [Pipeline APIs (e.g., RxGen)]
                 ⇒ [BRIDGE to Datalake]
```

### **4.3 Modules**

1. **Routes**:
   - `app.routes.studies`: Handles operations related to genomic studies.
   - `app.routes.variants`: Manages variant data within Beaker.
   - `app.routes.pipelines`: Integrates with bioinformatics pipelines.

2. **Services**:
   - `app.services.beaker_service`: Encapsulates MongoDB operations.
   - `app.services.pipeline_service`: Manages pipeline orchestration.
   - `app.services.bridge_service`: Orchestrates data loading into Datalake.

3. **Templates**:
   - `templates/studies.html`: UI for managing genomic studies.
   - `templates/variants.html`: UI for viewing and editing variants.
   - `templates/pipelines.html`: UI for pipeline status and controls.

4. **Utilities**:
   - Logging, validation, and common helpers for error handling and task execution.

## **5. Functionalities**

### **5.1 Beaker Management**

- **Subjects**:
  - Query all subjects in Beaker.
  - Add, update, or remove subjects.

- **Studies**:
  - View, edit, or add studies associated with subjects.
  - Provide detailed insights into study attributes and related variants.

- **Variants**:
  - List and edit variants linked to studies.
  - Search variants by `rsID`, chromosome, and position.

### **5.2 Pipeline Integration**

- **RxGen**:
  - Allow users to initiate pipeline runs.
  - Display real-time pipeline statuses and logs.

- **Pipeline Outputs**:
  - Provide mechanisms to review and validate pipeline-generated data.

### **5.3 Data Loading (BRIDGE)**

- **Control Panel**:
  - Launch and monitor data transfer processes from Beaker to Datalake.

- **Error Management**:
  - Capture and display errors encountered during the loading process.

- **Logging**:
  - Maintain comprehensive logs for auditing and debugging.

## **6. API Overview**

- **Beaker APIs**:
  - Query and update subjects, studies, and variants in MongoDB.

- **Pipeline APIs**:
  - Trigger pipeline runs and fetch pipeline statuses.

- **BRIDGE APIs**:
  - Initiate and monitor data loading to Datalake.

## **7. Security and Governance**

- Role-based access control to restrict operations to authorized users.
- Audit logs for all data changes and pipeline executions.
- SSL/TLS encryption for all data in transit.

## **8. Future Directions**

1. **Enhanced Visualizations**:
   - Add interactive dashboards to visualize genomic data.

2. **Modular Pipeline Integration**:
   - Expand support for additional pipelines.

3. **Enhanced BRIDGE Operations**:
   - Add configurable options for data transformations during loading.

4. **Reporting and Notifications**:
   - Enable automated email or Slack notifications for pipeline completions or errors.

## **9. Conclusion**

VitalEdge Flask focuses on providing a clean and efficient interface for managing Beaker data and orchestrating bioinformatics pipelines. By maintaining this dedicated scope, Flask ensures modularity and scalability, making it an essential component of the VitalEdge ecosystem.
